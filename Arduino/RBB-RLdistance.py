import serial
import time

def readdistance(port):
    rv=""
    while True:
     ch = port.read()
     if ch== '\r' or ch =='':
       return rv
     rv += ch
    
port = serial.Serial("/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_95635333430351D0E160-if00",baudrate=9600,timeout=3.0)

while True:
    string = readdistance(port)
    print"Distance:","R=",string.split(",")[0],"cm,L=",string.split(",")[1],"cm"
