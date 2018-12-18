import serial
import time

def readdistance(port):
    rv=""
    while True:
     ch = port.read()
     if ch== '\r' or ch =='':
       return rv
     rv += ch
    
port=serial.Serial("/dev/ttyACM0",baudrate=9600,timeout=3.0)

while True:
    string = readdistance(port)
    R = int(string.split(",")[0])
    L = int(string.split(",")[1])
    print "Distance:","R=",R,"cm,L",L,"cm"

    if R < 30 and L < 30:
       port.write('B')
       time.sleep(1)
    else:
        if L<30:
         port.write('4')
         time.sleep(1)
        elif R<30:
         port.write('2')
         time.sleep(1)
        else:
         port.write('F')
         time.sleep(1)

    
    
