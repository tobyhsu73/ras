#!/usr/bin/env python
#
# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3
#
# Copyright (c) 2016 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/BrickPi3/blob/master/LICENSE.md
#
# This code is an example for reading an EV3 gyro sensor connected to PORT_1 of the BrickPi3
# 
# Hardware: Connect an EV3 gyro sensor to BrickPi3 sensor port 1.
# 
# Results:  When you run this program, the gyro's absolute rotation and rate of rotation will be printed.

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''
import serial
import time     # import the time library for the sleep function
import brickpi3
ser=serial.Serial('/dev/ttyUSB0',9600)
ser.flushInput()

# import the BrickPi3 drivers
BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
def run():
  global x,y
  v = BP.get_sensor(BP.PORT_1)  
  
  y=v[0]
  y=y-x
  print(y)
  

# Configure for an EV3 color sensor.
# BP.set_sensor_type configures the BrickPi3 for a specific sensor.
# BP.PORT_1 specifies that the sensor will be on sensor port 1.
# BP.Sensor_TYPE.EV3_GYRO_ABS_DPS specifies that the sensor will be an EV3 gyro sensor.
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_GYRO_ABS_DPS)
x=0
while True:
  v = BP.get_sensor(BP.PORT_1)  
  if x==0:
      x=v[0]
  
  
  y=v[0]
  y=y-x
  ser.write(b'f')
  time.sleep(5)
  while y<87:
      ser.write(b'l')
      run()
      print('a')
      time.sleep(0.02)
  ser.write(b'f')
  time.sleep(2)
  while y<177:
      ser.write(b'l')
      run()
      time.sleep(0.02)
      print('b')
  ser.write(b'f')
  time.sleep(2)
  while y<267:
      ser.write(b'l')
      run()
      time.sleep(0.02)
      
  ser.write(b'f')
  time.sleep(2)
  while y<357:
      ser.write(b'l')
      run()
      time.sleep(0.02)
      
  time.sleep(2)
  
  # print the gyro sensor values
    
    