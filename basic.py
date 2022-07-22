# from base64 import encode
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import cv2 as cv
# import face_recognition

# imgelon = face_recognition.load_image_file("C:/Users/User/OneDrive/Desktop/images/em1.jpg")
# imgelon = cv.cvtColor(imgelon, cv.COLOR_BGR2RGB)

# imgtest = face_recognition.load_image_file("C:/Users/User/OneDrive/Desktop/images/bg1.jpg")
# imgtest = cv.cvtColor(imgtest, cv.COLOR_BGR2RGB)

# faceLoc = face_recognition.face_locations(imgelon)[0]
# encodeElon = face_recognition.face_encodings(imgelon)[0]
# cv.rectangle(imgelon,(faceLoc[3], faceLoc[0]),(faceLoc[1], faceLoc[2]), (255,0,255),2)

# faceLocTest = face_recognition.face_locations(imgtest)[0]
# encodeElonTest = face_recognition.face_encodings(imgtest)[0]
# cv.rectangle(imgtest,(faceLocTest[3], faceLocTest[0]),(faceLocTest[1], faceLocTest[2]), (255,0,255),2)

# results = face_recognition.compare_faces([encodeElon], encodeElonTest)
# faceDis = face_recognition.face_distance([encodeElon], encodeElonTest)
# print(results, faceDis)
# cv.putText(imgtest, f'{results} {round(faceDis[0],2)}',(50,50), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)

# cv.imshow('Elon mask', imgelon)
# cv.imshow('Elon test', imgtest)
# cv.waitKey(0)


import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # Flip camera vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()