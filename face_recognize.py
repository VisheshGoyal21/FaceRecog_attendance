from token import AMPER
import cv2
import numpy as np
from datetime import datetime

names = ['None', 'Vishesh', 'Sanyam', 'Vasu', 'Bhagwan', 'Kashin', 'Shivam']

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            datestring = now.strftime('%D')
            timestring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}, {datestring}, {timestring}')



cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray,
        scaleFactor = 1.1,
        minNeighbors = 10,
        minSize = (int(minW), int(minH)),
        )
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
        Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        if(confidence<100):
            Id = names[Id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            Id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            # Id="Unknown"
        # cv2.putText(im ,str(Id), (x,y+h), font, 255, 1)
        cv2.putText(im, str(Id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(im, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
        markAttendance(str(Id))
    cv2.imshow('im',im) 
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()