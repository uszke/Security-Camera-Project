import serial
import time

ser = serial.Serial()

ser.baudrate = 115200
ser.port = 'COM6'
ser.timeout = 0.5
ser.open()

while True:
    message = ser.read(b'BEL')
    print(message)

    time.sleep(0.5)