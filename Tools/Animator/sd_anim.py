"""make variations of input image"""

import argparse, os, sys, glob
import PIL
import torch
import numpy as np
import cv2

from color_matcher import ColorMatcher
from color_matcher.io_handler import load_img_file, save_img_file, FILE_EXTS
from color_matcher.normalizer import Normalizer

from omegaconf import OmegaConf
from random import randint
from PIL import Image
from tqdm import tqdm, trange
from itertools import islice
from einops import rearrange, repeat
from torchvision.utils import make_grid
from torch import autocast
from contextlib import nullcontext
import time
from pytorch_lightning import seed_everything

from ldm.util import instantiate_from_config
from ldm.models.diffusion.ddim import DDIMSampler
from ldm.models.diffusion.plms import PLMSSampler

#python Tools/Animator/sd_anim.py --prompt "Film test 1" --strength 0.42 --ddim_steps 80 --scale 8

def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())



def load_img(path):
    image = Image.open(path).convert("RGB")
    w, h = image.size
    print(f"loaded input image of size ({w}, {h}) from {path}")
    w, h = map(lambda x: x - x % 32, (w, h))  # resize to integer multiple of 32
    image = image.resize((w, h), resample=PIL.Image.LANCZOS)
    ImageObj = image
    image = np.array(image).astype(np.float32) / 255.0
    image = image[None].transpose(0, 3, 1, 2)
    image = torch.from_numpy(image)
    return (2.*image - 1., ImageObj)

cm = ColorMatcher()
prevLutImg = None

def setup_next_img(img, prevImg, lutImg, prevLutImg, sampleCount, CurrentSampleNum, curPromptInfo):
    
    
    w, h = img.size

    lutImg = lutImg.resize((w, h), resample=PIL.Image.LANCZOS)
    prevLutImg = prevLutImg.resize((w, h), resample=PIL.Image.Resampling.LANCZOS)

    lutImg = PIL.ImageChops.blend(prevLutImg, lutImg, (CurrentSampleNum+0.001)/ (sampleCount+0.001))

    img_src = np.array(img) 
    lut_Img = np.array(lutImg) 

    img_res = cm.transfer(src=img_src, ref=lut_Img, method='mkl')
    img_res = Normalizer(img_res).uint8_norm()

    #img2 = Image.fromarray(img_res)

    angle = curPromptInfo[3][0]
    zoom = curPromptInfo[3][1]
    translation_x = curPromptInfo[3][2]
    translation_y = curPromptInfo[3][3]
    print(
        f'angle: {angle}',
        f'zoom: {zoom}',
        f'translation_x: {translation_x}',
        f'translation_y: {translation_y}',
    )

    def make_xform_2d(width, height, translation_x, translation_y, angle, scale):
        center = (width // 2, height // 2)
        trans_mat = np.float32([[1, 0, translation_x], [0, 1, translation_y]])
        rot_mat = cv2.getRotationMatrix2D(center, angle, scale)
        trans_mat = np.vstack([trans_mat, [0,0,1]])
        rot_mat = np.vstack([rot_mat, [0,0,1]])
        return np.matmul(rot_mat, trans_mat)

    xform = make_xform_2d(w, h, translation_x, translation_y, angle, zoom)

    def sample_to_cv2(sample: torch.Tensor) -> np.ndarray:
        sample_f32 = rearrange(sample.squeeze().cpu().numpy(), "c h w -> h w c").astype(np.float32)
        sample_f32 = ((sample_f32 * 0.5) + 0.5).clip(0, 1)
        sample_int8 = (sample_f32 * 255).astype(np.uint8)
        return sample_int8

    def sample_from_cv2(sample: np.ndarray) -> torch.Tensor:
        sample = ((sample.astype(float) / 255.0) * 2) - 1
        sample = sample[None].transpose(0, 3, 1, 2).astype(np.float16)
        sample = torch.from_numpy(sample)
        return sample

    # transform previous frame
    #prev_img = sample_to_cv2(img2)
    prev_img = cv2.warpPerspective(
        img_res,
        xform,
        (img_res.shape[1], img_res.shape[0]),
        borderMode=cv2.BORDER_REPLICATE#cv2.BORDER_WRAP# if anim_args.border == 'wrap' else cv2.BORDER_REPLICATE
    )

    prev_img = Image.fromarray(prev_img) 

    image = np.array(prev_img).astype(np.float32) / 255.0
    image = image[None].transpose(0, 3, 1, 2)
    image = torch.from_numpy(image)
    return 2.*image - 1.



def main(args, model, progress_callback):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--prompt",
        type=str,
        nargs="?",
        default="a painting of a virus monster playing guitar",
        help="the prompt to render"
    )

    parser.add_argument(
        "--init-img",
        type=str,
        nargs="?",
        help="path to the input image",
        default="Tools/Animator/init_img/init.png"
    )

    parser.add_argument(
        "--outdir",
        type=str,
        nargs="?",
        help="dir to write results to",
        default="outputs/img2img-samples"
    )

    parser.add_argument(
        "--skip_grid",
        action='store_true',
        help="do not save a grid, only individual samples. Helpful when evaluating lots of samples",
    )

    parser.add_argument(
        "--skip_save",
        action='store_true',
        help="do not save indiviual samples. For speed measurements.",
    )

    parser.add_argument(
        "--ddim_steps",
        type=int,
        default=50,
        help="number of ddim sampling steps",
    )

    parser.add_argument(
        "--plms",
        action='store_true',
        help="use plms sampling",
    )
    parser.add_argument(
        "--fixed_code",
        action='store_true',
        help="if enabled, uses the same starting code across all samples ",
    )

    parser.add_argument(
        "--ddim_eta",
        type=float,
        default=0.0,
        help="ddim eta (eta=0.0 corresponds to deterministic sampling",
    )
    parser.add_argument(
        "--n_iter",
        type=int,
        default=1,
        help="sample this often",
    )
    parser.add_argument(
        "--C",
        type=int,
        default=4,
        help="latent channels",
    )
    parser.add_argument(
        "--f",
        type=int,
        default=8,
        help="downsampling factor, most often 8 or 16",
    )
    parser.add_argument(
        "--n_samples",
        type=int,
        default=1,
        help="how many samples to produce for each given prompt. A.k.a batch size",
    )
    parser.add_argument(
        "--n_rows",
        type=int,
        default=0,
        help="rows in the grid (default: n_samples)",
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=7,
        help="unconditional guidance scale: eps = eps(x, empty) + scale * (eps(x, cond) - eps(x, empty))",
    )

    parser.add_argument(
        "--strength",
        type=float,
        default=0.75,
        help="strength for noising/unnoising. 1.0 corresponds to full destruction of information in init image",
    )
    parser.add_argument(
        "--from-file",
        type=str,
        help="if specified, load prompts from this file",
    )
    parser.add_argument(
        "--config",
        type=str,
        default="configs/stable-diffusion/v1-inference.yaml",
        help="path to config which constructs model",
    )
    parser.add_argument(
        "--ckpt",
        type=str,
        default="models/ldm/stable-diffusion-v1/model.ckpt",
        help="path to checkpoint of model",
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="the seed (for reproducible sampling)",
    )
    parser.add_argument(
        "--precision",
        type=str,
        help="evaluate at this precision",
        choices=["full", "autocast"],
        default="autocast"
    )

    if args is None:
        args = parser.parse_args()

    opt = args
    print(opt)

    if opt.seed == None:
        opt.seed = randint(0, 1000000)
    print("init_seed = ", opt.seed)
    seed_everything(opt.seed)

    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    model = model.to(device)

    if opt.plms:
        raise NotImplementedError("PLMS sampler not (yet) supported")
        sampler = PLMSSampler(model)
    else:
        sampler = DDIMSampler(model)

    os.makedirs(opt.outdir, exist_ok=True)
    outpath = opt.outdir

    batch_size = opt.n_samples
    n_rows = opt.n_rows if opt.n_rows > 0 else batch_size
    '''
    if not opt.from_file:
        prompt = opt.prompts[0][0]
        assert prompt is not None
        data = [batch_size * [prompt]]

    else:
        print(f"reading prompts from {opt.from_file}")
        with open(opt.from_file, "r") as f:
            data = f.read().splitlines()
            data = list(chunk(data, batch_size))
    '''

    sample_path = os.path.join(outpath, f"anim_{opt.prompts[0][0]}")
    os.makedirs(sample_path, exist_ok=True)

    lut_path = os.path.join(sample_path, f"lut_{opt.prompts[0][0]}")
    os.makedirs(lut_path, exist_ok=True)

    lut_base_count = len(os.listdir(sample_path))

    base_count = len(os.listdir(sample_path))

    assert os.path.isfile(opt.init_img)
    init_image, init_image_pil = load_img(opt.init_img)
    init_image = init_image.to(device)
    #init_image = repeat(init_image, '1 ... -> b ...', b=batch_size)
    init_latent = model.get_first_stage_encoding(model.encode_first_stage(init_image))  # move to latent space

    sampler.make_schedule(ddim_num_steps=opt.ddim_steps, ddim_eta=opt.ddim_eta, verbose=False)


    sampleCount = 0
    imageCount = 0

    LUT_IMG = None
    PREV_LUT = init_image_pil 
    for promptIndex in range(len(opt.prompts)):
        curPrompt = opt.prompts[promptIndex][0]
        sampleCount = opt.prompts[promptIndex][2]

        try:
            nextPrompt = opt.prompts[promptIndex + 1][0]
        except:
            nextPrompt = curPrompt
        
        prompt = curPrompt

        data = [batch_size * [prompt]]
        nextData = [batch_size * [nextPrompt]]
                                           
        if(promptIndex != 0):
            PREV_LUT = LUT_IMG.convert("RGB")


        prev_init = init_image


        precision_scope = autocast if opt.precision=="autocast" else nullcontext
        with torch.no_grad():
            with precision_scope("cuda"):
                with model.ema_scope():
                    tic = time.time()
                    all_samples = list()
                    for n in trange(opt.n_iter, desc="Sampling"):
                        for prompts in tqdm(nextData, desc="data"):
                            uc = None
                            if opt.scale != 1.0:
                                uc = model.get_learned_conditioning(batch_size * [""])
                            if isinstance(prompts, tuple):
                                prompts = list(prompts)
                            c = model.get_learned_conditioning(prompts)
                            shape = [4, opt.H // 8, opt.W // 8]
                            samples_ddim, _ = sampler.sample(S=50,
                                                            conditioning=c,
                                                            batch_size=1,
                                                            shape=shape,
                                                            verbose=False,
                                                            unconditional_guidance_scale=opt.scale,
                                                            unconditional_conditioning=uc,
                                                            eta=opt.ddim_eta,
                                                            x_T=None)

                            x_samples_ddim = model.decode_first_stage(samples_ddim)
                            x_samples_ddim = torch.clamp((x_samples_ddim + 1.0) / 2.0, min=0.0, max=1.0)
                            x_samples_ddim = x_samples_ddim.cpu().permute(0, 2, 3, 1).numpy()

                            #x_checked_image, has_nsfw_concept = check_safety(x_samples_ddim) nsfw checker
                            x_checked_image = x_samples_ddim

                            x_checked_image_torch = torch.from_numpy(x_checked_image).permute(0, 3, 1, 2)

                            for x_sample in x_checked_image_torch:
                                x_sample = 255. * rearrange(x_sample.cpu().numpy(), 'c h w -> h w c')
                                img = Image.fromarray(x_sample.astype(np.uint8))
                                img.save(os.path.join(lut_path, f"{lut_base_count:05}.png"))
                                LUT_IMG = img.convert("RGB")
                                lut_base_count += 1
                   

                    toc = time.time()

        

        for i in range(0, int(sampleCount)):


            imageCount += 1
            print("\n")
            print(f"CURRENT PROMPT: {curPrompt}")
            print(f"CURRENT STRENGTH: {opt.prompts[promptIndex][1]}")
            print(f"Image #{imageCount}")
            print(f"Prompt Batch #{promptIndex+1}")
            print("\n")
            
            #seed_everything(randint(0, 1000000)) #TEST
            
            init_image = repeat(init_image, '1 ... -> b ...', b=batch_size)
            init_latent = model.get_first_stage_encoding(model.encode_first_stage(init_image))

            assert 0. <= opt.prompts[promptIndex][1] <= 1., 'can only work with strength in [0.0, 1.0]'
            t_enc = int(opt.prompts[promptIndex][1] * opt.ddim_steps)
            print(f"target t_enc is {t_enc} steps")

            precision_scope = autocast if opt.precision == "autocast" else nullcontext
            with torch.no_grad():
                with precision_scope("cuda"):
                    with model.ema_scope():
                        tic = time.time()
                        all_samples = list()
                        for n in trange(opt.n_iter, desc="Sampling"):
                            for prompts in tqdm(data, desc="data"):
                                uc = None
                                if opt.scale != 1.0:
                                    uc = model.get_learned_conditioning(batch_size * [""])
                                if isinstance(prompts, tuple):
                                    prompts = list(prompts)
                                c = model.get_learned_conditioning(prompts)

                                # encode (scaled latent)
                                z_enc = sampler.stochastic_encode(init_latent, torch.tensor([t_enc]*batch_size).to(device))
                                # decode it
                                samples = sampler.decode(z_enc, c, t_enc, unconditional_guidance_scale=opt.scale,
                                                        unconditional_conditioning=uc,)

                                x_samples = model.decode_first_stage(samples)
                                x_samples = torch.clamp((x_samples + 1.0) / 2.0, min=0.0, max=1.0)

                               
                                for x_sample in x_samples:
                                    x_sample = 255. * rearrange(x_sample.cpu().numpy(), 'c h w -> h w c')
                                    im = Image.fromarray(x_sample.astype(np.uint8))
                                    pathToCurImage = os.path.join(sample_path, f"{base_count:05}.png")
                                    im.save(pathToCurImage)
                                    progress_callback.emit(imageCount)
                                    base_count += 1
                                    #init_image = automatic_brightness_and_contrast(im)
                                    #init_image = Image.fromarray(init_image)
                                    init_image = setup_next_img(im, prev_init, LUT_IMG, PREV_LUT, sampleCount, i, opt.prompts[promptIndex]).to(device)
                                    prev_init = init_image
                                    print("Next Image\n\n")
                                all_samples.append(x_samples)

                        

                        toc = time.time()
                        

                    

    print(f"Your samples are ready and waiting for you here: \n{outpath} \n"
        f" \nEnjoy.")


if __name__ == "__main__":
    main()

