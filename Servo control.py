import serial
import time

ser = serial.Serial()

ser.baudrate = 115200
ser.port = 'COM6'
ser.timeout = 0.5
ser.open()

print(ser.name)

time.sleep(1)

while True:
    # ping
    ser.write(b'@')
    time.sleep(1)

    # 1st servo
    ser.write(b'0')
    ser.write('A'.encode('ascii'))  #A stands for a value of 97 or smth that is equal to and angular position of the servo

    time.sleep(1)

    ser.write(b'0')
    ser.write('z'.encode('ascii'))

    time.sleep(1)

    # 2nd servo
    ser.write(b'1')
    ser.write('A'.encode('ascii'))

    time.sleep(1)

    ser.write(b'1')
    ser.write('z'.encode('ascii'))

    time.sleep(1)