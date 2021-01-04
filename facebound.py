import cv2
import numpy as np
import imutils
from imutils.video import WebcamVideoStream
from easytello import tello
import time

def centrelocator(x, y, w, h):
    return int((2*x + w)/2), int((2*y +h)/2)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

mydrone = tello.Tello()
mydrone.send_command('streamon')
cap = imutils.video.WebcamVideoStream(src="udp://@0.0.0.0:11111").start()   # threading using imutils and opencv
#cap = cv2.VideoCapture(0)
mydrone.takeoff()

centre = centrelocator(0, 0, (cap.read()).shape[1],(cap.read()).shape[0])

while True:
    img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.circle(img, centre,8,(0, 255, 255), 18 )        # screen centre
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)      # face ROI
        cv2.circle(img, centrelocator(x, y, w, h), 9, (0, 255, 255), 18)        #  centre of ROI
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = img[y : y + h, x : x + w]
    time.sleep(0.3)     # needs to be threaded parallely to avoid shutdown
    mydrone.get_battery()
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

mydrone.land()
cap.stop()
cv2.destroyAllWindows()
