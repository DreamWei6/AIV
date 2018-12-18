import time
import serial

port = serial.Serial('/dev/ttyACM0', 9600, timeout = 3.0)

def stop():
    port.write(bytes('Q', 'UTF-8'))
    time.sleep(0.1)
def auto():
    port.write(bytes('T', 'UTF-8'))
    time.sleep(0.1)
def right():
    port.write(bytes('R', 'UTF-8'))
    time.sleep(0.1)
def left():
    port.write(bytes('L', 'UTF-8'))
    time.sleep(0.1)
def back():
    port.write(bytes('B', 'UTF-8'))
    time.sleep(0.1)
def forward():
    port.write(bytes('F', 'UTF-8'))
    time.sleep(0.1)

