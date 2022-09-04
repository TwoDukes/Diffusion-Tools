import argparse, os, sys, glob
import torch
import numpy as np
from random import randint
from omegaconf import OmegaConf
from PIL import Image
from tqdm import tqdm, trange
from itertools import islice
from einops import rearrange
from torchvision.utils import make_grid
import time
from pytorch_lightning import seed_everything
from torch import autocast
from contextlib import contextmanager, nullcontext

from ldm.util import instantiate_from_config
from ldm.models.diffusion.ddim import DDIMSampler
from ldm.models.diffusion.plms import PLMSSampler

from utils.generators import txt2img_generator, txt2img_generator_optimized

from diffusers.pipelines.stable_diffusion.safety_checker import StableDiffusionSafetyChecker
from transformers import AutoFeatureExtractor


# load safety model
safety_model_id = "CompVis/stable-diffusion-safety-checker"
safety_feature_extractor = AutoFeatureExtractor.from_pretrained(safety_model_id)
safety_checker = StableDiffusionSafetyChecker.from_pretrained(safety_model_id)


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def numpy_to_pil(images):
    """
    Convert a numpy image or a batch of images to a PIL image.
    """
    if images.ndim == 3:
        images = images[None, ...]
    images = (images * 255).round().astype("uint8")
    pil_images = [Image.fromarray(image) for image in images]

    return pil_images


def load_replacement(x):
    try:
        hwc = x.shape
        y = Image.open("assets/rick.jpeg").convert("RGB").resize((hwc[1], hwc[0]))
        y = (np.array(y)/255.0).astype(x.dtype)
        assert y.shape == x.shape
        return y
    except Exception:
        return x


def check_safety(x_image):
    safety_checker_input = safety_feature_extractor(numpy_to_pil(x_image), return_tensors="pt")
    x_checked_image, has_nsfw_concept = safety_checker(images=x_image, clip_input=safety_checker_input.pixel_values)
    assert x_checked_image.shape[0] == len(has_nsfw_concept)
    for i in range(len(has_nsfw_concept)):
        if has_nsfw_concept[i]:
            x_checked_image[i] = load_replacement(x_checked_image[i])
    return x_checked_image, has_nsfw_concept


def main(args, model, config, progress_callback):
       
    opt = args
    print(opt)

    if opt.laion400m:
        print("Falling back to LAION 400M model...")
        opt.config = "configs/latent-diffusion/txt2img-1p4B-eval.yaml"
        opt.ckpt = "models/ldm/text2img-large/model.ckpt"
        opt.outdir = "outputs/txt2img-samples-laion400m"

    if opt.seed == None:
        opt.seed = randint(0, 1000000)
    print("init_seed = ", opt.seed)
    seed_everything(opt.seed)

    sampler = None
    opt.device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    if(not opt.optimized):
        model = model.to(opt.device)

        if opt.plms:
            sampler = PLMSSampler(model)
        else:
            sampler = DDIMSampler(model)

    else:
        config.modelUNet.params.ddim_steps = opt.ddim_steps
        config.modelUNet.params.small_batch = True

        sampler = instantiate_from_config(config.modelUNet)
        _, _ = sampler.load_state_dict(model, strict=False)
        sampler.eval()
            
        samplerCS = instantiate_from_config(config.modelCondStage)
        _, _ = samplerCS.load_state_dict(model, strict=False)
        samplerCS.eval()
            
        samplerFS = instantiate_from_config(config.modelFirstStage)
        _, _ = samplerFS.load_state_dict(model, strict=False)
        samplerFS.eval()

        sampler=(sampler, samplerCS, samplerFS)

    os.makedirs(opt.outdir, exist_ok=True)
    outpath = opt.outdir

    opt.batch_size = opt.n_samples
    opt.n_rows = opt.n_rows if opt.n_rows > 0 else opt.batch_size
    if not opt.from_file:
        prompt = opt.prompt
        assert prompt is not None
        data = [opt.batch_size * [prompt]]
        opt.data = data

    else:
        print(f"reading prompts from {opt.from_file}")
        with open(opt.from_file, "r") as f:
            data = f.read().splitlines()
            data = list(chunk(data, opt.batch_size))
            opt.data = data

    sample_path = os.path.join(outpath, "samples")
    os.makedirs(sample_path, exist_ok=True)
    base_count = len(os.listdir(sample_path))
    grid_count = len(os.listdir(outpath)) - 1


    opt.start_code = None
    if opt.fixed_code:
        opt.start_code = torch.randn([opt.n_samples, opt.C, opt.H // opt.f, opt.W // opt.f], device=opt.device)

    progress_callback.emit(50)

    #generate images
    img = None
    if(opt.optimized):
        print("Using optimized generator")
        img = txt2img_generator_optimized(opt, model, config, sampler)
    else:
        print("Using default generator")
        img = txt2img_generator(opt, model, sampler)
    
    base_count+=1

    finalPath = os.path.join(sample_path, f"{base_count:05}.png")
    img.save(finalPath)

    print(f"Your samples are ready and waiting for you here: \n{outpath} \n"
          f" \nEnjoy.")

    return finalPath


if __name__ == "__main__":
    main()
