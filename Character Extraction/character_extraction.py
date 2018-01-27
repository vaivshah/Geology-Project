from PIL import ImageEnhance
from PIL import Image
import os
import cv2
import sys
import numpy as np


class Segmentation:

    def __init__(self, file_path, debug=False):
        """

        :param file_path: the location of the file, i.e. \dir\..\file.jpg
        """
        # Read image
        self.img = cv2.imread(file_path, 0)

        # Normalize the image
        self.img = np.float32(self.img) / 255.0

        # Convert image to numeric array
        self.img_array = np.asarray(self.img)

        self.debug = debug

    def printImage(self):
            if self.debug:
                self.debugImage()
            else:
                cv2.imshow('character', self.img)
                cv2.waitKey(1000)

    def debugImage(self):
        # img_array = self.img_array[168:2000, :]
        # print(img_array.shape)
        # im = Image.fromarray(img_array)
        # im.show()
        # # cv2.waitKey(40000)
        exit(69)


if __name__ == "__main__":
    yourpath = 'DataSet'
    for root, dirs, files in os.walk(yourpath, topdown=False):
        for imagefile in files:
            if imagefile.endswith(".jpg"):
                filepath = os.path.join(root, imagefile)
                image = Segmentation(file_path=filepath, debug=True)
                image.printImage()
