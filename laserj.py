from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division
import serial
import gartof
import brickpi3
import time
ser=serial.Serial('/dev/ttyUSB1',9600)
ser.flushInput()
BP = brickpi3.BrickPi3()
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_GYRO_ABS_DPS)# Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
def run():
  global x,y
  v = BP.get_sensor(BP.PORT_4)  
  
  y=v[0]
  y=y-x
  print(y)
x=0 
while True:
        # BP.get_sensor retrieves a sensor value.
        # BP.PORT_1 specifies that we are looking for the value of sensor port 1.
        # BP.get_sensor returns the sensor value (what we want to display).
        try:
            print(BP.get_sensor(BP.PORT_4))
            break# print the gyro sensor values
        except brickpi3.SensorError as error:
            print(error)
        
        time.sleep(0.02)  



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
        ser.write(b's')
        print('s')
    elif an>=100 and lld>=80and lrd>=80:
        ser.write(b'm')
        print('m')
    elif an<=50 and lld<=200 and lrd<=200:
        ser.write(b'n')
        print('n')
        ser.write(b'n')
        break
    elif ao<=50 and lld<=200and lrd<=200:
        print('n')
        ser.write(b'n')
        break
    
    else:
        ser.write(b'f')
        print('f')
run()
run()
while y<=87:
    run()
    ser.write(b'l')
    print('l')
    
while True:
    ser.write(b'f')
    print('f')

  
  
  