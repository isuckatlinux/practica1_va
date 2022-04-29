import os
import cv2
from matplotlib import pyplot
from Image import Image


class Warehouse:

    def __init__(self):
        self.train_images = []
        self.test_images = []

    def line_to_img(self, line: str, path):
        args = line.split(';')
        master_image = cv2.imread(path + '/' + args[0])
        minx = int(args[1])
        miny = int(args[2])
        maxx = int(args[3])
        maxy = int(args[4])
        cropped_img = master_image[miny:maxy, minx:maxx]
        img = Image(int(args[5]), cropped_img)
        return img

    def load_train_images(self, path):
        file = None
        if os.path.isdir(path):

            file = open(path + "/gt.txt", "r")
        else:
            raise Exception(f'File {path + "/gt.txt"} not found!')

        for line in file:
            self.train_images.append(self.line_to_img(line, path))


