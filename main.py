from ast import arg
from inspect import getargs
from locale import currency
from math import ceil, floor
import gc
import random
import sys
import glob
import os
import asyncio
import torch
import traceback
import cv2
from Tools.txt2img.txt2img import main as txt2img
from Tools.img2img.img2img import main as img2img
from Tools.Animator.sd_anim import main as txt2anim
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QFileDialog
from PySide2.QtCore import QFile, QTimer, QRunnable, Slot, Signal, QObject, QThreadPool
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QRunnable, Slot, QThreadPool
from ui.ui_main import Ui_MainWindow
from omegaconf import OmegaConf
from ldm.util import instantiate_from_config
from ui.DynamicElementBuilder import generateNewPromptBox


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

def load_model_from_config_optimized(ckpt, verbose=False):
    print(f"Loading model from {ckpt}")
    pl_sd = torch.load(ckpt, map_location="cpu")
    if "global_step" in pl_sd:
        print(f"Global Step: {pl_sd['global_step']}")
    sd = pl_sd["state_dict"]
    return sd

class dotdict(dict):    
        __getattr__ = dict.get
        __setattr__ = dict.__setitem__
        __delattr__ = dict.__delitem__

def loadSDModel(window, firstLoad=False):

    print("Loading SD Model")
    if(not window.ui.actionMenuOptimized.isChecked() and not firstLoad):
        return window.model, window.config

    configPath = 'configs/stable-diffusion/v1-inference.yaml'

    modelPath = 'models/ldm/stable-diffusion-v1/model.ckpt'

    config = OmegaConf.load(f"{configPath}")
    model = load_model_from_config(config, f"{modelPath}")

    window.ui.actionMenuStandard.setChecked(True)
    window.ui.actionMenuOptimized.setChecked(False)
   
    return model, config

def loadOptimizedSDModel(window):

    print("Loading Optimized SD Model")

    if(not window.ui.actionMenuStandard.isChecked()):
        return window.model, window.config

    configPath = 'configs/stable-diffusion/v1-inference_optimized.yaml'

    modelPath = 'models/ldm/stable-diffusion-v1/model.ckpt'

    config = OmegaConf.load(f"{configPath}")
    model = load_model_from_config_optimized(f"{modelPath}")
    li = []
    lo = []
    for key, value in model.items():
        sp = key.split('.')
        if(sp[0]) == 'model':
            if('input_blocks' in sp):
                li.append(key)
            elif('middle_block' in sp):
                li.append(key)
            elif('time_embed' in sp):
                li.append(key)
            else:
                lo.append(key)
    for key in li:
        model['model1.' + key[6:]] = model.pop(key)
    for key in lo:
        model['model2.' + key[6:]] = model.pop(key)

    window.ui.actionMenuStandard.setChecked(False)
    window.ui.actionMenuOptimized.setChecked(True)
   
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


def Generate_Image(args, previewLabel, window):                                                                                   
    print("GENERATING")

    def progress_fn(n):
        print(f"{n}% !!!!!!!!!!!!!!!!!!!!!!!")

    def setResult(curImage):
        #set init image line edit to cur image
        window.ui.img2imgInitPathLineEdit.setText(curImage)
        window.curImage_g = curImage
        SetInitLines(window)
        SetImageSize(args['W'], args['H'], previewLabel)
        SetPreviewImage(previewLabel, curImage)

    args = {
                'prompt': args['prompt'],
                'outdir':  args['outdir'],
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
                'precision':'autocast',
                'init_img': args['init_img'],
                'strength': args['strength'],
                'optimized': args['optimized']
            }

    args = dotdict(args)

    genMethod = img2img if window.ui.img2imgCheckbox.isChecked() else txt2img
    generationWorker = Worker(genMethod, args, window.model, window.config)

    generationWorker.signals.result.connect(setResult)
    generationWorker.signals.progress.connect(progress_fn)

    window.threadpool.start(generationWorker)


def Generate_Animation(args, previewLabel, window):
    print("GENERATING")

    print(args['prompts'])
    
    totalImageCount = 0
    for prompt in args['prompts']:
        totalImageCount += prompt[2]
    

    def progress_fn(curImage):
        
        window.ui.animCompletionProgressBar.setValue(floor((curImage/totalImageCount)*100))

        file_type = r'\*png'
        files = glob.glob(f"{args['outdir']}/anim_{args['prompts'][0][0]}" + file_type)
        max_file = max(files, key=os.path.getctime)
        window.curImage_g = max_file

        print(curImage)
        SetImageSize(args['W'], args['H'], previewLabel)
        SetPreviewImage(previewLabel, max_file)

    def setResult(curImage):
        SetInitLines(window)
        print("CREATING VIDEO")
        img_array = []
        file_type = r'\*png'
        for filename in glob.glob(f"{args['outdir']}/anim_{args['prompts'][0][0]}" + file_type):
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)
        
        fourcc = cv2.VideoWriter_fourcc(*'avc1')
        out = cv2.VideoWriter(f"{args['outdir']}/anim_{args['prompts'][0][0]}/animation.mp4",fourcc, 10, size)
 
        for i in range(len(img_array)):
            out.write(img_array[i])

        out.release()
        print("FINISHED")
 

    args = {
                'prompts': args['prompts'],
                'outdir':  args['outdir'],
                'skip_grid': None,
                'skip_save': None,
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
                'precision':'autocast',
                'init_img': args['init_img'],
                'strength': args['strength'],
                'optimized': args['optimized']
            }

    args = dotdict(args)

    genMethod = txt2anim
    generationWorker = Worker(genMethod, args, window.model, window.config)

    generationWorker.signals.result.connect(setResult)
    generationWorker.signals.progress.connect(progress_fn)

    window.threadpool.start(generationWorker)




# this function sets an image to a label
def SetPreviewImage(labelElement, imageURL):
    labelElement.setPixmap(QtGui.QPixmap(imageURL))

def SetInitLines(window):
    window.ui.img2imgInitPathLineEdit.setText(window.curImage_g)
    window.ui.animInitPathLineEdit.setText(window.curImage_g)
    
# this function sets a text to a label
def SliderChanged(args):
    args[1].setText(str(args[0]))

def SeedRandomize(seed, isRandom):
    if isRandom:
        seed.setText(str(random.randint(0, 999999999)))
    try:
        int(seed.text())
    except:
        print("Seed is not a number")
        seed.setText(str(random.randint(0, 999999999)))

    return seed.text()

def deleteLayout(cur_lay):
           
        if cur_lay is not None:
            while cur_lay.count():
                item = cur_lay.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    deleteLayout(item.layout())


def setFolderPath(fileLineEdit):
    filePath = QFileDialog.getExistingDirectory(None, "Select Directory")
    if filePath != "":
        fileLineEdit.setText(filePath)

def setFilePath(fileLineEdit, previewLabel=None):
    filePath = QFileDialog.getOpenFileName(None, "Select File")[0]
    if filePath != "":
        fileLineEdit.setText(filePath)
        if previewLabel != None:
            SetPreviewImage(previewLabel, fileLineEdit.text())

def SetImageSize(w,h,label):
    label.setMaximumHeight(h)
    label.setMinimumHeight(h)
    label.setMaximumWidth(w)
    label.setMinimumWidth(w)

def SwitchTabs(tabNumb, window):
    if tabNumb == 0:
        window.ui.mainStackedWidget.setCurrentIndex(0)
        window.ui.SecondaryStackedWidget.setCurrentIndex(0)
        window.ui.AnimatorTabButton.setChecked(False)

    elif tabNumb == 1:
        window.ui.mainStackedWidget.setCurrentIndex(1)
        window.ui.SecondaryStackedWidget.setCurrentIndex(1)
        window.ui.imageTabButton.setChecked(False)


def GetAnimPrompts(window):
    promptCount = window.ui.AnimatorMainVertLayoutGroup.count()
    prompts = []
    #example  ("bottles of champagne that explode into a characature wave of champagne",0.45, 60, (0.1, 1.01, -0.0, 0.0))
    for i in range(promptCount):
            curPromptLayout = window.ui.AnimatorMainVertLayoutGroup.itemAt(i)

            prompt = curPromptLayout.itemAt(1).widget().text()
            strength = curPromptLayout.itemAt(2).itemAt(0).widget().value()
            frames = curPromptLayout.itemAt(2).itemAt(1).widget().value()

            #skip 2 for lines

            zoom = curPromptLayout.itemAt(2).itemAt(4).widget().value()
            rotation = curPromptLayout.itemAt(2).itemAt(5).widget().value()
            xMotion = curPromptLayout.itemAt(2).itemAt(6).widget().value()
            yMotion = curPromptLayout.itemAt(2).itemAt(7).widget().value()

            curPrompt = (prompt,strength,frames,(rotation, zoom, xMotion, yMotion))
            print(curPrompt)
            prompts.append(curPrompt)

    return prompts


def getArgs(window, type = 0):
    if(type == 0): #Single Image
        args = {
            'prompt': window.ui.promptInput.text(),
            'steps': int(window.ui.stepsValueBox.text()),
            'scale': int(window.ui.scaleValueBox.text()),
            'imageCount': int(window.ui.imageCountValueBox.text()),
            'seed': SeedRandomize(window.ui.seedInputBox,window.ui.seedRandomized.isChecked()),
            'W': window.ui.widthInput.value(),
            'H': window.ui.heightInput.value(),
            'outdir': window.ui.imageOutputFolderLineEdit.text(),
            'strength': float(window.ui.strengthSlider.value())/100.0,
            'init_img': window.ui.img2imgInitPathLineEdit.text(),
            'prompts': GetAnimPrompts(window),
            'optimized': window.ui.actionMenuOptimized.isChecked()
        }
    elif(type == 1): #Animator (TODO)
        args = {
        'prompts': GetAnimPrompts(window),
        'steps': int(window.ui.animStepsSpinBox.value()),
        'scale': int(window.ui.animScaleSpinBox.value()),
        'imageCount': 1,
        'seed': SeedRandomize(window.ui.seedInputBox,window.ui.seedRandomized.isChecked()),
        'W': window.ui.widthInput.value(),
        'H': window.ui.heightInput.value(),
        'outdir': window.ui.imageOutputFolderLineEdit.text(),
        'strength': float(window.ui.strengthSlider.value())/100.0,
        'init_img': window.ui.animInitPathLineEdit.text(),
        'optimized': window.ui.actionMenuOptimized.isChecked()
        }
    return args
    


if __name__ == '__main__':
    app = QApplication(sys.argv)

    
    window = MainWindow()

    window.model = None
    window.config = None

    window.model, window.config = loadSDModel(window, True)

    def setModel(isOptimized, window):
        del window.model
        torch.cuda.empty_cache()
        
        gc.collect()
        
        print("Setting Model")
        if isOptimized:
            print("Optimized")
            window.model, window.config = loadOptimizedSDModel(window)
        else:
            print("Standard")
            window.model, window.config = loadSDModel(window)
        print("Model Set")





    window.ui.mainStackedWidget.setCurrentIndex(0)
    window.ui.SecondaryStackedWidget.setCurrentIndex(0)

    #Menu buttons
    window.ui.actionMenuStandard.triggered.connect(lambda: setModel(False, window))
    window.ui.actionMenuOptimized.triggered.connect(lambda: setModel(True, window))
    
    #Tab switching
    window.ui.imageTabButton.clicked.connect(lambda: SwitchTabs(0, window))
    window.ui.AnimatorTabButton.clicked.connect(lambda: SwitchTabs(1, window))


    ######### IMAGE TAB #########

    #sliders
    window.ui.stepSlider.valueChanged.connect(lambda: SliderChanged((window.ui.stepSlider.value()*5, window.ui.stepsValueBox)))
    window.ui.scaleSlider.valueChanged.connect(lambda: SliderChanged((window.ui.scaleSlider.value(), window.ui.scaleValueBox)))
    window.ui.imageCountSlider.valueChanged.connect(lambda: SliderChanged((window.ui.imageCountSlider.value(), window.ui.imageCountValueBox)))
    window.ui.strengthSlider.valueChanged.connect(lambda: SliderChanged((f"{window.ui.strengthSlider.value()}%", window.ui.strengthValueBox)))

    #buttons
    window.ui.imageOutputFolderButton.clicked.connect(lambda: setFolderPath(window.ui.imageOutputFolderLineEdit))
    window.ui.img2imgChoosefolder.clicked.connect(lambda: setFilePath(window.ui.img2imgInitPathLineEdit, window.ui.imagePreview))

    #generate button
    window.ui.generateButton.clicked.connect(lambda: Generate_Image(getArgs(window, 0), window.ui.imagePreview, window))
    
    SetPreviewImage(window.ui.imagePreview, 'ui/preview.png')

    ######### ANIMATOR TAB #########
    curAnimPromptCount = 1

    def makeNewPromptBox():
        global curAnimPromptCount
        curAnimPromptCount += 1
        generateNewPromptBox(window, curAnimPromptCount)

    def removePromptBox():
        global curAnimPromptCount
        curAnimPromptCount -= 1
        deleteLayout(window.ui.AnimatorMainVertLayoutGroup.takeAt(curAnimPromptCount))
        

    #buttons
    window.ui.animNewPromptButton.clicked.connect(lambda: makeNewPromptBox())
    window.ui.animRemovePromptButton.clicked.connect(lambda: removePromptBox())
    window.ui.animInitChooseFileButton.clicked.connect(lambda: setFilePath(window.ui.animInitPathLineEdit, window.ui.imagePreview))

    #generate button
    window.ui.startAnimationButton.clicked.connect(lambda: Generate_Animation(getArgs(window, 1), window.ui.imagePreview, window))


    window.show()

    sys.exit(app.exec_())