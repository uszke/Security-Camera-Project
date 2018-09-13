import numpy as np
import cv2
import serial
import time


ser = serial.Serial()



class camera:
    def __init__(self, setupPan, setupTilt, setPan, setTilt, panDegree, tiltDegree, haarFace):
        self.setupPan = setupPan # X AXIS SETUP
        self.setupTilt = setupTilt # Y AXIS SETUP
        self.setPan = setPan # SETTING THE X SERVO STARTING POINT
        self.setTilt = setTilt # SETTING THE Y SERVO STARTING POINT
        self.panDegree = panDegree
        self.tiltDegree = tiltDegree
        self.haarFace = haarFace
    def setpantilt(self):
        ser.write(bytearray([self.setupPan, self.setPan]))
        ser.write(bytearray([self.setupTilt, self.setTilt]))
    def detection(self):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


        faces = face_cascade.detectMultiScale(gray, 1.1, 3)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]


            if (self.setPan > 120 & self.setPan < 200):
                print('Standby')
            if (self.setTilt > 70 & self.setTilt < 140):
                print('Standby')
            if (self.setPan > 250):
                self.panDegree -= 2
                camera.setpantilt(self.panDegree, self.tiltDegree)
            if (self.setPan < 100):
                self.panDegree += 2
                camera.setpantilt(self.panDegree, self.tiltDegree)
            if (self.setTilt > 30):
                self.tiltDegree += 2
                camera.setpantilt(self.panDegree, self.tiltDegree)
            if (self.setTilt < 180):
                self.tiltDegree -= 2
                camera.setpantilt(self.panDegree, self.tiltDegree)

            cv2.imshow('img', img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break


class pir:
    pass

class arduino:
    #ser = serial.Serial(port='COM3', baudrate=115200, open=True)

    def __init__(self, baudrate, port):
        self.baudrate = baudrate
        self.port = port

    def setup(self):
        ser.baudrate = self.baudrate
        ser.port = self.port


# setupPan = Servo '0' address, setupTilt  = Servo '1' address, setPan = Start position, setTilt  = Start position
# panDegree = Controls sweeping, tiltdegree = controls tilting, haarFace = haarcascade frontalface xml file
cameraSetup = camera(48, 49, 90, 40, 90, 40, 'haarcascade_frontalface_default.xml')
arduinoSetup = arduino(115200, 'COM3')
arduino.setup(arduinoSetup)
ser.open()
cap = cv2.VideoCapture(1)

while 1:
    camera.detection(cameraSetup)




cap.release()
cv2.destroyAllWindows()
