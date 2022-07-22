import cv2
import numpy as np
cam=cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id=input('enter your id: ')
sampleNum=0

while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        sampleNum=sampleNum+1
        cv2.imwrite("images/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('frame',img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
# break if the sample number is morethan 20
    elif sampleNum>50:
        break

cam.release()
cv2.destroyAllWindows()




# import cv2
# import numpy as np
# import os

# camera = cv2.VideoCapture(0)
# camera.set(3, 640)
# camera.set(4, 480)

# face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# face_id = input('\n enter user id end press <return> ==>  ')

# print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# # Initialize individual sampling face count
# count = 0

# while(True):
    
#     ret, img = camera.read()
#     img = cv2.flip(img, -1) # flip video image vertically
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_detector.detectMultiScale(gray, 1.3, 5)

#     for (x,y,w,h) in faces:

#         cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
#         count += 1

#         # Save the captured image into the datasets folder
#         cv2.imwrite("images/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

#         cv2.imshow('image', img)

#     k = cv2.waitKey(0) & 0xff # Press 'ESC' for exiting video
#     if k == 27:
#         break
#     elif count >= 30: # Take 30 face sample and stop video
#          break

# # Do a bit of cleanup
# print("\n [INFO] Exiting Program and cleanup stuff")
# camera.release()
# cv2.destroyAllWindows()

# if not camera.isOpened():
#     print("The camera is not operand... Exiting")
#     exit()

# Labels = ["Vishesh", "Surbhi"]

# for label in Labels:
#     if not os.path.exists(label):
#         os.mkdir(label)
    

# for folder in Labels:
#     #using count variable to name the images in the dataset.
#     count = 0
#     #Taking input to start the capturing
#     print("Press 's' to start data collection for "+folder)
#     userinput = input()
#     if userinput != 's':
#         print("Wrong Input..........")
#         exit()
#     #clicking 200 images per label, you could change as you want.    
#     while count<100:
#         #read returns two values one is the exit code and other is the frame
#         status, frame = camera.read()
#         #check if we get the frame or not
#         if not status:
#             print("Frame is not been captured..Exiting...")
#             break
#         #convert the image into gray format for fast caculation
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         #display window with gray image
#         cv2.imshow("Video Window",gray)
#         #resizing the image to store it
#         gray = cv2.resize(gray, (64,64))
#         #Store the image to specific label folder
#         cv2.imwrite('C:/Users/User/python/minor_project/images/'+folder+'/img'+str(count)+'.jpg',gray)
#         count=count+1
#         #to quite the display window press 'q'
#         if cv2.waitKey(1) == ord('q'):
#             break
# # When everything done, release the capture
# camera.release()
# cv2.destroyAllWindows()