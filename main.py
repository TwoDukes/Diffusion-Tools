import sys
import asyncio
from Tools.txt2img.txt2img import main as txt2img
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from ui.ui_main import Ui_MainWindow


class dotdict(dict):    
        __getattr__ = dict.get
        __setattr__ = dict.__setitem__
        __delattr__ = dict.__delitem__

def main():
   
    print('main')
    

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



def Generate_txt2img(args):                                                                                   
    print("GENERATING")

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
                'n_samples': 1,
                'n_rows': 0,
                'scale': args['scale'],
                'from_file': None,
                'config': 'configs/stable-diffusion/v1-inference.yaml', 
                'ckpt': 'models/ldm/stable-diffusion-v1/model.ckpt',
                'seed': None,
                'precision':'autocast'
            }

    args = dotdict(args)
    asyncio.run(txt2img(args))
    
def SliderChanged(args):
    args[1].setText(f"{args[2]}: {str(args[0])}")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    window.ui.stepSlider.valueChanged.connect(lambda: SliderChanged((window.ui.stepSlider.value(), window.ui.stepCountLabel, 'STEP COUNT')))
    window.ui.scaleSlider.valueChanged.connect(lambda: SliderChanged((window.ui.scaleSlider.value(), window.ui.scaleCountLabel, 'SCALE')))
    window.ui.generateButton.clicked.connect(lambda: Generate_txt2img({
        'prompt': window.ui.promptInput.text(),
        'steps': window.ui.stepSlider.value(),
        'scale': window.ui.scaleSlider.value()
    }))

    #main()

    window.show()

    sys.exit(app.exec_())