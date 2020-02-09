import time
import cv2
import numpy as np
import os
from datetime import datetime

if __name__ == '__main__':
    try:

        # Camera settimgs
        cam_width = 320
        cam_height = 240

        # Final image capture settings
        scale_ratio = 0.5
        # Camera resolution height must be dividable by 16, and width by 32
        cam_width = int((cam_width+31)/32)*32
        cam_height = int((cam_height+15)/16)*16
        print ("Used camera resolution: "+str(cam_width)+" x "+str(cam_height))

        # Initialize cameras and settings
        camera1 = cv2.VideoCapture(1)
        print("Setting the custom Width and Height")
        camera1.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
        camera1.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

        camera2 = cv2.VideoCapture(2)
        print("Setting the custom Width and Height")
        camera2.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
        camera2.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

        t2 = datetime.now()
        counter = 0
        avgtime = 0

        while True:
            # Read Camera 1
            check1, frame1 = camera1.read()
            # Convert frame to gray scale image
            # frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

            # Read Camera 2
            check2, frame2 = camera2.read()
            # Convert frame to gray scale image
            # frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

            counter+=1
            t1 = datetime.now()
            timediff = t1-t2
            avgtime = avgtime + (timediff.total_seconds())
            cv2.imshow("pair1", frame1)
            cv2.imshow("pair2", frame2)

            # Wait one millisecond and captures a new frame
            key = cv2.waitKey(15) & 0xFF
            t2 = datetime.now()

    except KeyboardInterrupt:
        avgtime = avgtime / counter
        print("Average time between frames: " + str(avgtime))
        print("Average FPS: " + str(1 / avgtime))
        if (os.path.isdir("./scenes") == False):
            os.makedirs("./scenes")
        cv2.imwrite('C:\\Users\\98ale\\PycharmProjects\\stereo_imaging\\scenes\\photo1.png', frame1)
        cv2.imwrite('C:\\Users\\98ale\\PycharmProjects\\stereo_imaging\\scenes\\photo2.png', frame2)
        camera1.release()
        camera2.release()
        exit()