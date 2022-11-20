import numpy as np
import cv2


def capture():
    cap = cv2.VideoCapture(0)
    img_counter = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("failed capture")
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) == ord('q'):
            break

        if cv2.waitKey(1)%256 == 32:
            img = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img, frame)
            print("took")
            img_counter +=1

    cap.release()
    cv2.destroyAllWindows()