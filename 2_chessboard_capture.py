import time
import cv2
import numpy as np
import os
from datetime import datetime

if __name__ == '__main__':
    try:

        # Photo session settings
        total_photos = 30             # Number of images to take
        countdown = 5                 # Interval for count-down timer, seconds
        font=cv2.FONT_HERSHEY_SIMPLEX # Cowntdown timer font

        # Camera settimgs
        cam_width = 320
        cam_height = 240

        # Final image capture settings
        scale_ratio = 0.5
        # Camera resolution height must be dividable by 16, and width by 32
        cam_width = int((cam_width+31)/32)*32
        cam_height = int((cam_height+15)/16)*16
        print ("Used camera resolution: "+str(cam_width)+" x "+str(cam_height))

        # Initialize Camera 1 & Set height/width
        camera1 = cv2.VideoCapture(1)
        print("Setting the custom Width and Height")
        camera1.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
        camera1.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

        # Initialize Camera 2 & Set height/width
        camera2 = cv2.VideoCapture(2)
        print("Setting the custom Width and Height")
        camera2.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
        camera2.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

        # Start Capturing Images
        counter = 0
        t2 = datetime.now()
        if (os.path.isdir("./pairs")==False):
          os.makedirs("./pairs")
        print ("Starting photo sequence")

        while True:
            # Read Camera 1
            check1, frame1 = camera1.read()
            # Convert frame to gray scale image
            # frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

            # Read Camera 2
            check2, frame2 = camera2.read()
            # Convert frame to gray scale image
            # frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

            t1 = datetime.now()
            cntdwn_timer = countdown - int ((t1-t2).total_seconds())
            # If cowntdown is zero - let's record next image
            if cntdwn_timer == -1:
              counter += 1

              filename1 = './pairs/left_'+str(counter).zfill(2)+'.png'
              cv2.imwrite(filename1, frame1)
              filename2 = './pairs/right_'+str(counter).zfill(2)+'.png'
              cv2.imwrite(filename2, frame2)

              print (' ['+str(counter)+' of '+str(total_photos)+'] '+filename1)
              print (' ['+str(counter)+' of '+str(total_photos)+'] '+filename2)

              t2 = datetime.now()
              time.sleep(1)
              cntdwn_timer = 0      # To avoid "-1" timer display
              next
            # Draw cowntdown counter, seconds
            cv2.putText(frame1, str(cntdwn_timer), (50,50), font, 2.0, (0,0,255),4, cv2.LINE_AA)
            cv2.putText(frame2, str(cntdwn_timer), (50,50), font, 2.0, (0,0,255),4, cv2.LINE_AA)
            cv2.imshow("pair1", frame1)
            cv2.imshow("pair2", frame2)
            key = cv2.waitKey(1) & 0xFF

            # Wait till all photos are taken
            if (counter == total_photos):
              break

    except KeyboardInterrupt:
        camera1.release()
        camera2.release()
        exit()