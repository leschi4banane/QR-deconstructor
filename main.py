import sys
import cv2

class QrReader():
    def __init__(self, path) -> None:
        img = cv2.imread(path)
        cv2.imshow('image', img)
        cv2.waitKey(0)

if __name__ == '__main__':
    args = sys.argv
    qr = QrReader(args[1])