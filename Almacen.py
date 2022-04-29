import os
import cv2
from matplotlib import pyplot
from Image import Image
from Image import SignalType
from tqdm import tqdm

width_image = 50
height_image = 50

class Warehouse:

    def __init__(self):
        self.train_images = {SignalType.PROHIBIDO:[], SignalType.PELIGRO:[], SignalType.STOP:[], SignalType.DIRECCION_PROHIBIDA:[], SignalType.CEDA_EL_PASO:[], SignalType.DIRECCION_OBLIGATORIA:[], SignalType.OTRA:[]}
        self.test_images = []

    def line_to_img(self, line: str, path):
        args = line.split(';')
        master_image = cv2.imread(path + '/' + args[0])
        minx = int(args[1])
        miny = int(args[2])
        maxx = int(args[3])
        maxy = int(args[4])
        cropped_img = master_image[miny:maxy, minx:maxx]
        resized_img = cv2.resize(cropped_img, (width_image, height_image), interpolation = cv2.INTER_AREA)
        img = Image(int(args[5]), cropped_img)
        return img

    
    def load_train_images(self, path):
        if not os.path.isdir(path):
            raise Exception(f'File {path + "/gt.txt"} not found!')
        print('Cargando datos...')
        gt_file = path + '/gt.txt'
        num_lines = sum(1 for line in open(gt_file,'r'))
        with open(gt_file, 'r') as f:
            for i, line in enumerate(tqdm(f, total=num_lines)):
                img = self.line_to_img(line, path)
                self.train_images[img.signal_type].append(img)