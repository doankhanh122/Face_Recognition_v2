import cv2 as cv
import PIL.Image as Image
import numpy as np
import face_recognition
import os
import threading, _thread


# COLOR
FACE_RECTANGLE_COLOR = (0, 255, 0)

# Message
ONLY_ONE_PERSON_CAUTION = 'ERROR, ONLY ON PERSON ONE TIME'

# Key constant
ESC = 27  # ESC
PRIMARY_KEY = 81
SECOND_KEY = 113

# CONSTANT
TITLE = 'AGR FACE RECOGNITION'

# DIRECTORY
PATH = 'data'


data = {}


# TODO FACE detection
def faces_location(frame_rgn):
    locations = face_recognition.face_locations(frame_rgb)  # Return a List
    return locations


# Make Rectangle
def draw_rectangle(frame_, loc):
    cv.rectangle(frame_, (loc[3], loc[0]), (loc[1], loc[2]), color=FACE_RECTANGLE_COLOR, thickness=2)

# TODO Make a class for create new Thread
class MyThread (threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.locations = []

    # play webcam
    def face_detection(self, frame_to_detect):
        locations = face_recognition.face_locations(frame_to_detect)
        # print(locations)
        self.locations = locations
        print(self.locations)


# TODO turn on webcam
webcam = cv.VideoCapture(0)
# # Setup Revolution
# webcam.set(3, 300)
# webcam.set(4, 400)

# Make new thread
mythread = MyThread('Thread-1','face detection')
mythread.start()
while True:
    success, frame = webcam.read()

    # Convert to rgb
    rgb_frame = frame[:, :, ::-1]

    # frame = cv.flip(frame, 1)

    # # Face Detection
    # face_locations = face_recognition.face_locations(gray_scale)
    # # print(face_locations)
    # # Draw rectangle to face
    # for face_location in face_locations:
    #     cv.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]),
    #                  color=FACE_RECTANGLE_COLOR,
    #                  thickness=2)
    #
    # # Encoding face
    # encoded_face = face_recognition.face_encodings(rgb_frame, face_locations)

    # Starting a new Thread

    mythread.face_detection(rgb_frame)
    for face_location in mythread.locations:
        cv.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]),
                     color=FACE_RECTANGLE_COLOR,
                     thickness=2)

    cv.imshow(TITLE, frame)
    key = cv.waitKey(1)
    if key == ESC or key == SECOND_KEY or key == ESC:
        break


