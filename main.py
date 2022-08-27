from math import ceil, floor
import random
import sys
import asyncio
import torch
from Tools.txt2img.txt2img import main as txt2img
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2 import QtCore, QtGui, QtWidgets
from ui.ui_main import Ui_MainWindow
from omegaconf import OmegaConf
from ldm.util import instantiate_from_config

config_g = None
model_g = None

def load_model_from_config(config, ckpt, verbose=False):
    print(f"Loading model from {ckpt}")
    pl_sd = torch.load(ckpt, map_location="cpu")
    if "global_step" in pl_sd:
        print(f"Global Step: {pl_sd['global_step']}")
    sd = pl_sd["state_dict"]
    model = instantiate_from_config(config.model)
    m, u = model.load_state_dict(sd, strict=False)
    if len(m) > 0 and verbose:
        print("missing keys:")
        print(m)
    if len(u) > 0 and verbose:
        print("unexpected keys:")
        print(u)

    model.cuda()
    model.eval()
    return model

class dotdict(dict):    
        __getattr__ = dict.get
        __setattr__ = dict.__setitem__
        __delattr__ = dict.__delitem__

def loadSDModel():

    modelPath = 'models/ldm/stable-diffusion-v1/model.ckpt'
    configPath = 'configs/stable-diffusion/v1-inference.yaml'

    config = OmegaConf.load(f"{configPath}")
    model = load_model_from_config(config, f"{modelPath}")
   
    return model, config
    

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



def Generate_txt2img(args, previewLabel):                                                                                   
    print("GENERATING")
    SetPreviewImage(previewLabel, 'ui/loading.png')

    args = {
                'prompt': args['prompt'],
                'outdir':  'Outputs/txt2img-samples',
                'skip_grid': None,
                'skip_save': None,
                'ddim_steps': args['steps'],
                'plms': None,
                'laion400m': False,
                'fixed_code': None,
                'ddim_eta': 0.0,
                'n_iter': 1,
                'H': 512,
                'W': 512,
                'C': 4,
                'f': 8,
                'n_samples': args['imageCount'],
                'n_rows': int(floor(float(args['imageCount'])/2)),
                'scale': args['scale'],
                'from_file': None,
                'config': 'configs/stable-diffusion/v1-inference.yaml', 
                'ckpt': 'models/ldm/stable-diffusion-v1/model.ckpt',
                'seed': int(args['seed']),
                'precision':'autocast'
            }

    args = dotdict(args)
    curImage = txt2img(args, model_g, config_g)
    print(curImage)
    SetPreviewImage(previewLabel, curImage)

# this function sets an image to a label
def SetPreviewImage(labelElement, imageURL):
    labelElement.setPixmap(QtGui.QPixmap(imageURL))
    
# this function sets a text to a label
def SliderChanged(args):
    args[1].setText(f"{args[2]}: {str(args[0])}")

def SeedRandomize(seed, isRandom):
    if isRandom:
        seed.setText(str(random.randint(0, 999999999)))
    try:
        int(seed.text())
    except:
        print("Seed is not a number")
        seed.setText(str(random.randint(0, 999999999)))

    return seed.text()
    


if __name__ == '__main__':
    app = QApplication(sys.argv)

    model_g, config_g = loadSDModel()

    window = MainWindow()

    window.ui.stepSlider.valueChanged.connect(lambda: SliderChanged((window.ui.stepSlider.value(), window.ui.stepCountLabel, 'STEP COUNT')))
    window.ui.scaleSlider.valueChanged.connect(lambda: SliderChanged((window.ui.scaleSlider.value(), window.ui.scaleCountLabel, 'SCALE')))
    window.ui.imageCountSlider.valueChanged.connect(lambda: SliderChanged((window.ui.imageCountSlider.value(), window.ui.imageAmountLabel, 'IMAGES')))
    window.ui.generateButton.clicked.connect(lambda: Generate_txt2img({
        'prompt': window.ui.promptInput.text(),
        'steps': window.ui.stepSlider.value(),
        'scale': window.ui.scaleSlider.value(),
        'imageCount': window.ui.imageCountSlider.value(),
        'seed': SeedRandomize(window.ui.seedInputBox,window.ui.seedRandomized.isChecked())
    },window.ui.imagePreview))
    
    SetPreviewImage(window.ui.imagePreview, 'ui/preview.png')


    window.show()

    sys.exit(app.exec_())