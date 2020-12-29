import cv2 as cv
# CONSTANT
TITLE = 'AGR FACE RECOGNITION'
# Key constant
ESC = 27  # ESC
PRIMARY_KEY = 81
SECOND_KEY = 113


webcam = cv.VideoCapture(0)
while True:
    success, frame = webcam.read()
    # frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    rgb_fram = frame[:, :, ::-1]

    cv.imshow(TITLE, frame_rgb)
    key = cv.waitKey(1)
    if key == ESC or key == SECOND_KEY or key == ESC:
        break
