import cv2
import numpy as np
cap = cv2.VideoCapture(1)
i = 0

if str(raw_input("Ready? (Y/N)")) == "Y":
    while i<21:
        ret, frame = cap.read()
        if ret == True:
            cv2.imwrite(str(i)+".jpg",frame.astype(np.uint8))
            i += 1
        else:
            print("Ret is false")
cv2.waitKey(0)
