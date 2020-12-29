import cv2 as cv
import numpy as np
import face_recognition


# TODO Load the image
imgDaniel = face_recognition.load_image_file('faces_train/Daniel/5.jpg')
imgDaniel = cv.cvtColor(imgDaniel, cv.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('faces_train/Daniel/2.jpg')
imgTest = cv.cvtColor(imgTest, cv.COLOR_BGR2RGB)

# TODO Finding face
faceLoc = face_recognition.face_locations(imgDaniel)[0]
encodeDaniel = face_recognition.face_encodings(imgDaniel)[0]
cv.rectangle(imgDaniel, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 255, 255), thickness=2)
print(encodeDaniel)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeDanielTest = face_recognition.face_encodings(imgTest)[0]
cv.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (0, 255, 255), thickness=2)

# TODO Compare encoding
results = face_recognition.compare_faces([encodeDaniel], encodeDanielTest)
print(results)

# TODO find the best match
faceDis = face_recognition.face_distance([encodeDaniel], encodeDanielTest)
print(faceDis)

# TODO input text to face regtangle
cv.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50,50), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), thickness=2)

cv.imshow('Daniel', imgDaniel)
cv.imshow('DANIEL TEST', imgTest)












cv.waitKey(0)