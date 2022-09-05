"""make variations of input image"""

import argparse, os, sys, glob
import PIL
import torch
import numpy as np
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

from utils.generators import img2img_generator, img2img_generator_optimized


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def load_img(path):
    image = Image.open(path).convert("RGB")
    w, h = image.size
    print(f"loaded input image of size ({w}, {h}) from {path}")
    w, h = map(lambda x: x - x % 32, (w, h))  # resize to integer multiple of 32
    image = image.resize((w, h), resample=PIL.Image.LANCZOS)
    image = np.array(image).astype(np.float32) / 255.0
    image = image[None].transpose(0, 3, 1, 2)
    image = torch.from_numpy(image)
    return 2.*image - 1.0


def main(args, model, window, progress_callback):
    
    opt = args

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
    if not opt.from_file:
        prompt = opt.prompt
        assert prompt is not None
        opt.data = [opt.batch_size * [prompt]]

    else:
        print(f"reading prompts from {opt.from_file}")
        with open(opt.from_file, "r") as f:
            data = f.read().splitlines()
            opt.data = list(chunk(data, opt.batch_size))

    sample_path = os.path.join(outpath, "samples")
    os.makedirs(sample_path, exist_ok=True)
    base_count = len(os.listdir(sample_path))

    assert os.path.isfile(opt.init_img)
    init_image = load_img(opt.init_img).to(opt.device)

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


    

    assert 0. <= opt.strength <= 1., 'can only work with strength in [0.0, 1.0]'
    opt.t_enc = int(opt.strength * opt.ddim_steps)
    print(f"target t_enc is {opt.t_enc} steps")

    finalPath = None

    progress_callback.emit(50)

    #generate images
    img = None
    if not opt.optimized:
        img = img2img_generator(opt, init_latent, model, sampler)
    else:
        img = img2img_generator_optimized(opt, init_latent, model, sampler)

    base_count+=1

    finalPath = os.path.join(sample_path, f"{base_count:05}.png")
    img.save(finalPath)

    print(f"Your samples are ready and waiting for you here: \n{outpath} \n"
          f" \nEnjoy.")
    return finalPath

if __name__ == "__main__":
    main()
