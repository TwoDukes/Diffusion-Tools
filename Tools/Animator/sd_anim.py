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

from utils.generators import txt2img_generator, img2img_generator, txt2img_generator_optimized, img2img_generator_optimized

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
    return 2.*image - 1.0, ImageObj

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



def main(args, model, window, progress_callback):
    parser = argparse.ArgumentParser()

    opt = args
    print(opt)

    if opt.seed == None:
        opt.seed = randint(0, 1000000)
    print("init_seed = ", opt.seed)
    seed_everything(opt.seed)

    sampler = None
    opt.device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    if(not opt.optimized):
        model = model.to(opt.device)

        if opt.plms:
            raise NotImplementedError("PLMS sampler not (yet) supported")
            sampler = PLMSSampler(model)
        else:
            sampler = DDIMSampler(model)

    else:
        sampler = (model[0], model[1], model[2])

    os.makedirs(opt.outdir, exist_ok=True)
    outpath = opt.outdir

    opt.batch_size = opt.n_samples
    n_rows = opt.n_rows if opt.n_rows > 0 else opt.batch_size


    sample_path = os.path.join(outpath, f"anim_{opt.prompts[0][0]}")
    os.makedirs(sample_path, exist_ok=True)

    lut_path = os.path.join(sample_path, f"lut_{opt.prompts[0][0]}")
    os.makedirs(lut_path, exist_ok=True)

    lut_base_count = len(os.listdir(sample_path))

    base_count = len(os.listdir(sample_path))

    assert os.path.isfile(opt.init_img)
    init_image, init_image_pil = load_img(opt.init_img)
    init_image = init_image.to(opt.device)

    init_latent = None
    if not opt.optimized:
        init_image = repeat(init_image, '1 ... -> b ...', b=opt.batch_size)
        init_latent = model.get_first_stage_encoding(model.encode_first_stage(init_image)) 
        sampler.make_schedule(ddim_num_steps=opt.ddim_steps, ddim_eta=opt.ddim_eta, verbose=False)
    else:  
        sampler[2].to(opt.device)
        init_image = repeat(init_image, '1 ... -> b ...', b=opt.batch_size)
        init_latent = sampler[2].get_first_stage_encoding(sampler[2].encode_first_stage(init_image))  # move to latent space
        sampler[0].make_schedule(ddim_num_steps=opt.ddim_steps, ddim_eta=opt.ddim_eta, verbose=False)


    sampleCount = 0
    imageCount = 0

    LUT_IMG = None
    PREV_LUT = init_image_pil 
    for promptIndex in range(len(opt.prompts)):

        if(window.stopThread):
            return

        curPrompt = opt.prompts[promptIndex][0]
        sampleCount = opt.prompts[promptIndex][2]

        try:
            nextPrompt = opt.prompts[promptIndex + 1][0]
        except:
            nextPrompt = curPrompt
        
        prompt = curPrompt

        opt.data = [opt.batch_size * [nextPrompt]]
                                           
        if(promptIndex != 0):
            PREV_LUT = LUT_IMG.convert("RGB")


        prev_init = init_image

        #generate LUT
        img = None
        if(not opt.optimized):
            img = txt2img_generator(opt, model, sampler)
        else:
            img = txt2img_generator_optimized(opt, model, sampler)

        img.save(os.path.join(lut_path, f"{lut_base_count:05}.png"))
        LUT_IMG = img.convert("RGB")
        lut_base_count += 1

        opt.data = [opt.batch_size * [prompt]]

        

        for i in range(0, int(sampleCount)):

            if(window.stopThread):
                return

            imageCount += 1
            print("\n")
            print(f"CURRENT PROMPT: {curPrompt}")
            print(f"CURRENT STRENGTH: {opt.prompts[promptIndex][1]}")
            print(f"Image #{imageCount}")
            print(f"Prompt Batch #{promptIndex+1}")
            print("\n")
            
            #seed_everything(randint(0, 1000000)) #TEST
            
            init_image = repeat(init_image, '1 ... -> b ...', b=opt.batch_size)
            init_latent = None
            if not opt.optimized:
                init_image = repeat(init_image, '1 ... -> b ...', b=opt.batch_size)
                init_latent = model.get_first_stage_encoding(model.encode_first_stage(init_image)) 
                #sampler.make_schedule(ddim_num_steps=opt.ddim_steps, ddim_eta=opt.ddim_eta, verbose=False)
            else:  
                opt.seed = randint(0, 1000000)
                seed_everything(opt.seed)

                sampler[2].to(opt.device)
                init_image = repeat(init_image, '1 ... -> b ...', b=opt.batch_size)
                init_latent = sampler[2].get_first_stage_encoding(sampler[2].encode_first_stage(init_image))  # move to latent space
                #sampler[0].make_schedule(ddim_num_steps=opt.ddim_steps, ddim_eta=opt.ddim_eta, verbose=False)


            assert 0. <= opt.prompts[promptIndex][1] <= 1., 'can only work with strength in [0.0, 1.0]'
            opt.t_enc = int(opt.prompts[promptIndex][1] * opt.ddim_steps)
            print(f"target t_enc is {opt.t_enc} steps")
            
            #generate frame
            im = None
            if not opt.optimized:
                im = img2img_generator(opt, init_latent, model, sampler)
            else:
                im = img2img_generator_optimized(opt, init_latent, model, sampler)

                                    
            pathToCurImage = os.path.join(sample_path, f"{base_count:05}.png")
            im.save(pathToCurImage)
            progress_callback.emit(imageCount)
            base_count += 1
            init_image = setup_next_img(im, prev_init, LUT_IMG, PREV_LUT, sampleCount, i, opt.prompts[promptIndex]).to(opt.device)
            prev_init = init_image
            print("Next Image\n\n")
     

    print(f"Your samples are ready and waiting for you here: \n{outpath} \n"
        f" \nEnjoy.")


if __name__ == "__main__":
    main()

