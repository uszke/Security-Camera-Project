import numpy as np
import cv2
import serial
import time


# Just saving serial.Serial() as ser. So we only need to call ser
ser = serial.Serial()

# Setting up the connection between Arduino and Python
def setup():
    ser.baudrate = 115200
    ser.port = 'COM6' # Which COM port the arduino is connected to.
    ser.open() # Opening the ports

# Setting up control of the servos
def setpantilt(x,y):
    ser.write(bytearray([48, x]))
    ser.write(bytearray([49, y]))


setup() # Calling the setup function / setting up Arduino
setpantilt(90, 25) # Setting X & Y starting position
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # Loading the XML haarcascade file
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') # Loading the XML haarcascade file
#full_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml') # Loading the XML haarcascade file

cap = cv2.VideoCapture(1) # Opens and saves the video feed into a variable, 'cap'

# Normal variables which later becomes
tiltX = 90
tiltY = 25


time.sleep(1)
while 1:


    ret, img = cap.read()
    #gray = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]


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
        if(y > 60):
            tiltY += 2
            setpantilt(tiltX, tiltY)
        if(y < 150):
            tiltY -= 2
            setpantilt(tiltX, tiltY)







    # Opens the video frame
    cv2.imshow('Security Camera', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()