import serial
import time

ser = serial.Serial()

ser.baudrate = 115200
ser.port = 'COM6'
ser.timeout = 0.5
ser.open()

print(ser.name)
#ser.read(b'r')
time.sleep(1)

while ser.read(b'r'):
    # ping
    ser.write(b'@')
    time.sleep(1)

    #ser.read(b'r')

    # 1st servo horizonal
    ser.write(b'0')
    ser.write('0'.encode('ascii'))  #A stands for a value of 97 or smth that is equal to an angular position of the servo

    time.sleep(1)

    ser.write(b'0')
    ser.write('a'.encode('ascii'))

    time.sleep(0.5)

    # 2nd servo vertical
    ser.write(b'1')
    ser.write('0'.encode('ascii'))

    time.sleep(0.5)

    ser.write(b'1')
    ser.write('z'.encode('ascii'))

    #ser.read(b'r')
    #ser.write('1'.encode('ascii'))

    time.sleep(0.5)

  #  print(ser.read(b'r'))