import cv2
import numpy as np
import sys
import os

PACK_DIR = os.path.abspath('./kerasYolo/')
sys.path.append(PACK_DIR)

from kerasYolo.yolo import YOLO

helmet_yolo = YOLO(model_path='~',
            anchors_path='~',
            classes_path='~')

def cam():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 10)
    cap.set(3, 416)
    cap.set(4, 416)

    while True:
        ret, frame = cap.read()
        frame1 = Image.fromarray(frame)
        
        cv2.imshow('video', frame)
        out_boxes, out_scores, out_classes, classes_names = helmet_yolo.detect_image(frame1)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cv2.destroyAllWindows()

cam()