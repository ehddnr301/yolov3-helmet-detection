import cv2
import numpy as np

def cam():
    cap = cv2.VideoCapture(0)
    cap.set(3, 416)
    cap.set(4, 416)

    while True:
        ret, frame = cap.read()
        
        cv2.imshow('video', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cv2.destroyAllWindows()

cam()