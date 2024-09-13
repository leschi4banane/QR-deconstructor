import sys
from typing import List
import cv2
import numpy as np

class QrReader():
    def __init__(self, path) -> None:
        cv2_img = cv2.imread(path)
        self.img_width = cv2_img.shape[1]
        self.img_height = cv2_img.shape[0]
        
        img = self.black_white(cv2_img)
        img = self.cut(img)
        cv2.imshow('code', self.to_cv2(img))
        
        cv2.waitKey(0)
        
    def black_white(self, cv2_img) -> List[List[int]]:
        img = np.full((self.img_width, self.img_height), False, dtype=bool)
        
        for x in range(0, self.img_width):
            for y in range(0, self.img_height):
                av = (int(cv2_img[y, x, 0]) + int(cv2_img[y, x, 1]) + int(cv2_img[y, x, 2])) / 3
                if av < 128:
                    img[y, x] = True
                else:
                    img[y, x] = False
        return img
        
    def cut(self, img):
        min_x = self.img_width
        min_y = self.img_height
        max_x = 0
        max_y = 0
        
        for x in range(0, self.img_width):
            for y in range(0, self.img_height):
                if img[y, x] == True:
                    min_x = min(min_x, x)
                    max_x = max(max_x, x)
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)

        return img[min_x:max_x, min_y:max_y]
        
    def to_cv2(self, img):
        cv2_img = np.full((len(img[0]), len(img), 3), 0, dtype=np.uint8)
        
        for x in range(0, len(img[0])):
            for y in range(0, len(img)):
                if img[y, x] == True:
                    cv2_img[y, x] = [0, 0, 0]
                else:
                    cv2_img[y, x] = [255, 255, 255]
        return cv2_img
    
        

if __name__ == '__main__':
    args = sys.argv
    qr = QrReader(args[1])