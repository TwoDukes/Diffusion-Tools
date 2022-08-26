import PySimpleGUI as sg
import asyncio
from Tools.txt2img.txt2img import main as txt2img

'''
    Example of GUI
'''

class dotdict(dict):    
        __getattr__ = dict.get
        __setattr__ = dict.__setitem__
        __delattr__ = dict.__delitem__

def main():
    sg.theme('Dark')

    layout = [
        [sg.Text('SD TOOLS', size=(30, 1), font=("Helvetica", 25))],
        [sg.Text('TXT2IMG')],
        [sg.InputText('Enter your prompt here...', key='in1')],
        [sg.Slider(range=(1, 150), orientation='h', size=(34, 20), key='slide1', default_value=50)], 
        [sg.Text('STEP COUNT')],
        [sg.Slider(range=(1, 20), orientation='h', size=(34, 20), key='slide2', default_value=7)],
        [sg.Text('CFG SCALE')],
        
       
        [sg.Button('Generate')],
        [sg.Text('_' * 80)],
        [sg.Text('Choose A Folder', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), justification='right'),
         sg.InputText('Default Folder', key='folder'), sg.FolderBrowse()],
        [sg.Button('Exit'),
         sg.Text(' ' * 40), sg.Button('SaveSettings'), sg.Button('LoadSettings')]
    ]

    window = sg.Window('SD Tools', layout, default_element_size=(50, 1), grab_anywhere=False)

    while True:
        event, values = window.read()

        if event == 'SaveSettings':
            filename = sg.popup_get_file('Save Settings', save_as=True, no_window=True)
            window.SaveToDisk(filename)
            # save(values)
        elif event == 'LoadSettings':
            filename = sg.popup_get_file('Load Settings', no_window=True)
            window.LoadFromDisk(filename)
            # load(form)
        elif event == 'Generate':
            args = {
                'prompt': values['in1'],
                'outdir':  'Outputs/txt2img-samples',
                'skip_grid': None,
                'skip_save': None,
                'ddim_steps': int(values['slide1']),
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
                'scale': float(values['slide2']),
                'from_file': None,
                'config': 'configs/stable-diffusion/v1-inference.yaml', 
                'ckpt': 'models/ldm/stable-diffusion-v1/model.ckpt',
                'seed': None,
                'precision':'autocast'
            }
            args = dotdict(args)

            asyncio.run(txt2img(args))

            # load(form)
        elif event in ('Exit', None):
            break

    window.close()

    


if __name__ == '__main__':
    main()