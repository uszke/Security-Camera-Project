import numpy as np
import cv2
import serial
import time

ser = serial.Serial()

for pos in range (80,300,5):
    standby = pos

def setup():
    ser.baudrate = 115200
    ser.port = 'COM6'
    ser.open()


def setpantilt(x,y):
    ser.write(bytearray([48, x]))
    ser.write(bytearray([49, y]))


setup()
setpantilt(90, 40)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#full_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
cap = cv2.VideoCapture(1)


tiltX = 90
tiltY = 40


time.sleep(1)
while 1:


    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        print('X :', x, 'Y :', y)

        if (x > 120 & x < 200):
            print('Standby')
        if (y > 70 & y < 140):
            print('Standby')
        if (x > 250):
            tiltX -= 2
            setpantilt(tiltX, tiltY)
        if (x < 100):
            tiltX += 2
            setpantilt(tiltX, tiltY)
        if(y > 30):
            tiltY += 2
            setpantilt(tiltX, tiltY)
        if(y < 180):
            tiltY -= 2
            setpantilt(tiltX, tiltY)
        else:
            break







    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()