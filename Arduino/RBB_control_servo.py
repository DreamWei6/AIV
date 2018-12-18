import serial
import time


port=serial.Serial('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_95635333430351D0E160-if00',baudrate=9600,timeout=3.0)

while True:

    port.write('B')
    time.sleep(1)

    port.write('R')
    time.sleep(1)

    port.write('L')
    time.sleep(1)

    port.write('F')
    time.sleep(1)

    exit()
