# Import the openCV module
import cv2

# Triggers the local camera
video = cv2.VideoCapture(2)

while True:
    # First parameter is a boolean that checks if the video can be read
    # Second parameter is a numPy array of the frame
    video_check, frame = video.read()

    # This is a gray scale image of the frame. We choose to convert it
    # for the benefits of less information processed for each pixel
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Shows a pop-up window with the video
    cv2.imshow('Image Window', image)

    # Wait one millisecond and captures a new frame
    key = cv2.waitKey(1)

    # Exits the loop when 'c' is pressed
    if key == ord('c'):
        break

video.release()
cv2.destroyAllWindows()