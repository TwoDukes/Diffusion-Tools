from ast import arg
from math import ceil, floor
import random
import sys
import asyncio
import torch
import traceback
from Tools.txt2img.txt2img import main as txt2img
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget
from PySide2.QtCore import QFile, QTimer, QRunnable, Slot, Signal, QObject, QThreadPool
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QRunnable, Slot, QThreadPool
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
    

#------------------WORKER------------------

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()

#------------------WORKER------------------
#------------------UI------------------

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())



def Generate_txt2img(args, previewLabel, window):                                                                                   
    print("GENERATING")
    SetPreviewImage(previewLabel, 'ui/loading.png')

    def progress_fn(n):
        print(f"{n}%")

    def setResult(curImage):
        SetPreviewImage(previewLabel, curImage)

    args = {
                'prompt': args['prompt'],
                'outdir':  'Outputs/txt2img-samples',
                'skip_grid': None,
                'skip_save': True,
                'ddim_steps': args['steps'],
                'plms': None,
                'laion400m': False,
                'fixed_code': None,
                'ddim_eta': 0.0,
                'n_iter': 1,
                'H': args['H'],
                'W': args['W'],
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
    generationWorker = Worker(txt2img, args, model_g)
    #curImage = txt2img(args, model_g, config_g)
    #generationWorker.run()
    generationWorker.signals.result.connect(setResult)
    generationWorker.signals.progress.connect(progress_fn)

    window.threadpool.start(generationWorker)
    #print(curImage)
    #SetPreviewImage(previewLabel, curImage)



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

    window.ui.stepSlider.valueChanged.connect(lambda: SliderChanged((window.ui.stepSlider.value()*5, window.ui.stepCountLabel, 'STEP COUNT')))
    window.ui.scaleSlider.valueChanged.connect(lambda: SliderChanged((window.ui.scaleSlider.value(), window.ui.scaleCountLabel, 'SCALE')))
    window.ui.imageCountSlider.valueChanged.connect(lambda: SliderChanged((window.ui.imageCountSlider.value(), window.ui.imageAmountLabel, 'IMAGES')))
    window.ui.generateButton.clicked.connect(lambda: Generate_txt2img({
        'prompt': window.ui.promptInput.text(),
        'steps': window.ui.stepSlider.value()*5,
        'scale': window.ui.scaleSlider.value(),
        'imageCount': window.ui.imageCountSlider.value(),
        'seed': SeedRandomize(window.ui.seedInputBox,window.ui.seedRandomized.isChecked()),
        'W': window.ui.widthInput.value(),
        'H': window.ui.heightInput.value(),
    },window.ui.imagePreview, window))
    
    SetPreviewImage(window.ui.imagePreview, 'ui/preview.png')


    window.show()

    sys.exit(app.exec_())