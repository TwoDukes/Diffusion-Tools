import argparse, os, sys, glob
import torch
import numpy as np

from omegaconf import OmegaConf
from random import randint
from PIL import Image
from tqdm import tqdm, trange
from einops import rearrange, repeat
from torchvision.utils import make_grid
from torch import autocast
from contextlib import nullcontext
import time
from pytorch_lightning import seed_everything

from ldm.util import instantiate_from_config
from ldm.models.diffusion.ddim import DDIMSampler
from ldm.models.diffusion.plms import PLMSSampler

def txt2img_generator(opt, model, sampler):
    precision_scope = autocast if opt.precision=="autocast" else nullcontext
    with torch.no_grad():
        with precision_scope("cuda"):
            with model.ema_scope():
                tic = time.time()
                all_samples = list()
                for n in trange(opt.n_iter, desc="Sampling"):
                    for prompts in tqdm(opt.data, desc="data"):
                        uc = None
                        if opt.scale != 1.0:
                            uc = model.get_learned_conditioning(opt.batch_size * [""])
                        if isinstance(prompts, tuple):
                            prompts = list(prompts)
                        c = model.get_learned_conditioning(prompts)
                        shape = [opt.C, opt.H // opt.f, opt.W // opt.f]
                        samples_ddim, _ = sampler.sample(S=opt.ddim_steps,
                                                         conditioning=c,
                                                         batch_size=opt.n_samples,
                                                         shape=shape,
                                                         verbose=False,
                                                         unconditional_guidance_scale=opt.scale,
                                                         unconditional_conditioning=uc,
                                                         eta=opt.ddim_eta,
                                                         x_T=opt.start_code)

                        x_samples_ddim = model.decode_first_stage(samples_ddim)
                        x_samples_ddim = torch.clamp((x_samples_ddim + 1.0) / 2.0, min=0.0, max=1.0)
                        x_samples_ddim = x_samples_ddim.cpu().permute(0, 2, 3, 1).numpy()

                        #x_checked_image, has_nsfw_concept = check_safety(x_samples_ddim) nsfw checker
                        x_checked_image = x_samples_ddim

                        x_checked_image_torch = torch.from_numpy(x_checked_image).permute(0, 3, 1, 2)

                        for x_sample in x_checked_image_torch:
                            x_sample = 255. * rearrange(x_sample.cpu().numpy(), 'c h w -> h w c')
                            img = Image.fromarray(x_sample.astype(np.uint8))

                            return img

                toc = time.time()

def img2img_generator(opt, init_latent, model, sampler):
    precision_scope = autocast if opt.precision == "autocast" else nullcontext
    with torch.no_grad():
        with precision_scope("cuda"):
            with model.ema_scope():
                tic = time.time()
                all_samples = list()
                for n in trange(opt.n_iter, desc="Sampling"):
                    for prompts in tqdm(opt.data, desc="data"):
                        uc = None
                        if opt.scale != 1.0:
                            uc = model.get_learned_conditioning(opt.batch_size * [""])
                        if isinstance(prompts, tuple):
                            prompts = list(prompts)
                        c = model.get_learned_conditioning(prompts)

                        # encode (scaled latent)
                        z_enc = sampler.stochastic_encode(init_latent, torch.tensor([opt.t_enc]*opt.batch_size).to(opt.device))
                        # decode it
                        samples = sampler.decode(z_enc, c, opt.t_enc, unconditional_guidance_scale=opt.scale,
                                                 unconditional_conditioning=uc,)

                        x_samples = model.decode_first_stage(samples)
                        x_samples = torch.clamp((x_samples + 1.0) / 2.0, min=0.0, max=1.0)


                        for x_sample in x_samples:
                            x_sample = 255. * rearrange(x_sample.cpu().numpy(), 'c h w -> h w c')
                            img = Image.fromarray(x_sample.astype(np.uint8))
                            return img           

                toc = time.time()


def txt2img_generator_optimized(opt, model, sampler):

    
    if opt.precision == "autocast":
        sampler[0].half()
        sampler[1].half()

    precision_scope = autocast if opt.precision=="autocast" else nullcontext
    with torch.no_grad():

        all_samples = list()
        for n in trange(opt.n_iter, desc="Sampling"):
            for prompts in tqdm(opt.data, desc="data"):
                with precision_scope("cuda"):
                    sampler[1].to(opt.device)
                    uc = None
                    if opt.scale != 1.0:
                        uc = sampler[1].get_learned_conditioning(opt.batch_size * [""])
                    if isinstance(prompts, tuple):
                        prompts = list(prompts)
                    
                    c = sampler[1].get_learned_conditioning(prompts)
                    shape = [opt.C, opt.H // opt.f, opt.W // opt.f]
                    mem = torch.cuda.memory_allocated()/1e6
                    sampler[1].to("cpu")
                    while(torch.cuda.memory_allocated()/1e6 >= mem):
                        time.sleep(1)


                    samples_ddim = sampler[0].sample(S=opt.ddim_steps,
                                    conditioning=c,
                                    batch_size=opt.n_samples,
                                    seed = opt.seed,
                                    shape=shape,
                                    verbose=False,
                                    unconditional_guidance_scale=opt.scale,
                                    unconditional_conditioning=uc,
                                    eta=opt.ddim_eta,
                                    x_T=opt.start_code)

                    sampler[2].to(opt.device)
                    print("saving images")
                    for i in range(opt.batch_size):
                        
                        x_samples_ddim = sampler[2].decode_first_stage(samples_ddim[i].unsqueeze(0))
                        x_sample = torch.clamp((x_samples_ddim + 1.0) / 2.0, min=0.0, max=1.0)
                        x_sample = 255. * rearrange(x_sample[0].cpu().numpy(), 'c h w -> h w c')
                        img = Image.fromarray(x_sample.astype(np.uint8))
                        return img

                        #potentially move return img under mem clear
                        mem = torch.cuda.memory_allocated()/1e6
                        samplerFS.to("cpu")
                        while(torch.cuda.memory_allocated()/1e6 >= mem):
                            time.sleep(1)
                        del samples_ddim
                        print("memory_final = ", torch.cuda.memory_allocated()/1e6)

        toc = time.time()

def img2img_generator_optimized(opt, init_latent, model, sampler): 
    '''
    if opt.precision == "autocast":
        sampler[0].half()
        sampler[1].half()
        sampler[2].half()
        init_image = init_image.half()
    

    mem = torch.cuda.memory_allocated()/1e6
    sampler[2].to("cpu")
    while(torch.cuda.memory_allocated()/1e6 >= mem):
        time.sleep(1)
    '''  



    precision_scope = autocast if opt.precision=="autocast" else nullcontext
    with torch.no_grad():

        all_samples = list()
        for n in trange(opt.n_iter, desc="Sampling"):
            for prompts in tqdm(opt.data, desc="data"):
                with precision_scope("cuda"):
                    sampler[1].to(opt.device)
                    uc = None
                    if opt.scale != 1.0:
                        uc = sampler[1].get_learned_conditioning(opt.batch_size * [""])
                    if isinstance(prompts, tuple):
                        prompts = list(prompts)
                    
                    c = sampler[1].get_learned_conditioning(prompts)
                    mem = torch.cuda.memory_allocated()/1e6
                    sampler[1].to("cpu")
                    while(torch.cuda.memory_allocated()/1e6 >= mem):
                        time.sleep(1)

                    # encode (scaled latent)
                    z_enc = sampler[0].stochastic_encode(init_latent, torch.tensor([opt.t_enc]*opt.batch_size).to(opt.device), opt.seed)
                    # decode it
                    samples_ddim = sampler[0].decode(z_enc, c, opt.t_enc, unconditional_guidance_scale=opt.scale,
                                                unconditional_conditioning=uc,)


                    sampler[2].to(opt.device)
                    print("saving images")
                    for i in range(opt.batch_size):
                        
                        x_samples_ddim = sampler[2].decode_first_stage(samples_ddim[i].unsqueeze(0))
                        x_sample = torch.clamp((x_samples_ddim + 1.0) / 2.0, min=0.0, max=1.0)
                        x_sample = 255. * rearrange(x_sample[0].cpu().numpy(), 'c h w -> h w c')
                        img = Image.fromarray(x_sample.astype(np.uint8))

                        return img


                        mem = torch.cuda.memory_allocated()/1e6
                        sampler[2].to("cpu")
                        while(torch.cuda.memory_allocated()/1e6 >= mem):
                            time.sleep(1)

                        del samples_ddim
                        print("memory_final = ", torch.cuda.memory_allocated()/1e6)