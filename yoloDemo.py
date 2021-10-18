import numpy as np
import cv2

cap = cv2.VideoCapture(0) # index of web came

classesFile = 'coco.names'
classNames = []
with open(classesFile, 'rt') as f:
    classNames = f.read()

#classes = ['car', 'drone']

while True:
    success, img = cap.read()

    cv2.imshow('Image', img)
    cv2.waitKey(1)


