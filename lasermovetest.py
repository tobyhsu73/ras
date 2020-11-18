import serial
import gartof
import time


ser=serial.Serial('/dev/ttyUSB1',9600)
ser.flushInput()
time.sleep(5)
while True:
    
    tofdata = gartof.tofget()
    lrd = tofdata[0]['distance']
    lrs = tofdata[0]['status']
    lld = tofdata[2]['distance']
    lls = tofdata[2]['status']
    print(lld,lls,lrd,lrs)
    an = lrd-lld
    ao = lld-lrd
    if lld>=1000 or lrd>=1000:
        ser.write(b'n')
        print(b'n')
    elif ao >=100 and lld>=80 and lrd>=80:
        ser.write(b'r')
        print('r')
    elif an>=100 and lld>=80and lrd>=80:
        ser.write(b'l')
        print('l')
    elif an<=50 and lld<=90 and lrd<=90:
        ser.write(b'n')
        print('n')
        ser.write(b'n')
    elif ao<=50 and lld<=150and lrd<=150:
        print('n')
        ser.write(b'n')
    
    else:
        ser.write(b'f')
        print('f')
        