import cv2
import numpy as np
import sys
import os
import time

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
        start = time.time()
        ret, frame = cap.read()
        frame1 = Image.fromarray(frame)
        
        out_boxes, out_scores, out_classes, classes_names = helmet_yolo.detect_image(frame1)

        for i, c in reversed(list(enumerate(out_classes))):
            predicted_classes = classes_names[c]
            box = out_boxes[i]
            score = out_scores[i]

            y1, x1, y2, x2 = box
            y1 = max(0, np.floor(y1 + 0.5).astype('int32'))
            x1 = max(0, np.floor(x1 + 0.5).astype('int32'))
            y2 = max(416, np.floor(y2 + 0.5).astype('int32'))
            x2 = max(416, np.floor(x2 + 0.5).astype('int32'))

            box_color = (255,0,0) if c == 0 else (0,0,255)
            cv2.rectangle(frame, (x1,y1), (x2, y2), box_color)



        cv2.imshow('video', frame)
        
        end = time.time()
        s = end - start
        print(f'{s} second')

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cv2.destroyAllWindows()

cam()