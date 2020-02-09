import os
import cv2
import numpy as np
import json
from stereovision.calibration import StereoCalibrator
from stereovision.calibration import StereoCalibration
from stereovision.exceptions import ChessboardNotFoundError

# Global variables preset
total_photos = 30
photo_width = 640
photo_height = 240
img_width = 320
img_height = 240
image_size = (img_width, img_height)

# Chessboard parameters
rows = 6
columns = 9
square_size = 2.5

calibrator = StereoCalibrator(rows, columns, square_size, image_size)
photo_counter = 0
print('Start cycle')

while photo_counter != total_photos:
    photo_counter = photo_counter + 1
    print('Import pair No ' + str(photo_counter))
    leftName = './pairs/left_' + str(photo_counter).zfill(2) + '.png'
    rightName = './pairs/right_' + str(photo_counter).zfill(2) + '.png'
    if os.path.isfile(leftName) and os.path.isfile(rightName):
        imgLeft = cv2.imread(leftName, 1)
        imgRight = cv2.imread(rightName, 1)
        try:
            calibrator._get_corners(imgLeft)
            calibrator._get_corners(imgRight)
        except ChessboardNotFoundError as error:
            print(error)
            print("Pair No " + str(photo_counter) + " ignored")
        else:
            calibrator.add_corners((imgLeft, imgRight), True)

print('End cycle')

print('Starting calibration... It can take several minutes!')
calibration = calibrator.calibrate_cameras()
calibration.export('calib_result')
print('Calibration complete!')

# Lets rectify and show last pair after  calibration
calibration = StereoCalibration(input_folder='calib_result')
rectified_pair = calibration.rectify((imgLeft, imgRight))

cv2.imshow('Left CALIBRATED', rectified_pair[0])
cv2.imshow('Right CALIBRATED', rectified_pair[1])
cv2.imwrite("rectifyed_left.jpg", rectified_pair[0])
cv2.imwrite("rectifyed_right.jpg", rectified_pair[1])
cv2.waitKey(0)