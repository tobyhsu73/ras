# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/BrickPi3/blob/master/LICENSE.md
#
# This code is an example for reading an EV3 ultrasonic sensor connected to PORT_1 of the BrickPi3
# 
# Hardware: Connect an EV3 ultrasonic sensor to BrickPi3 sensor port 1.
# 
# Results:  When you run this program, the ultrasonic sensor distance will be printed.

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# Configure for an EV3 color sensor.
# BP.set_sensor_type configures the BrickPi3 for a specific sensor.
# BP.PORT_1 specifies that the sensor will be on sensor port 1.
# BP.Sensor_TYPE.EV3_ULTRASONIC_CM specifies that the sensor will be an EV3 ultrasonic sensor.
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)# Configure for an EV3 ultrasonic sensor.

try:
    while True:
        # BP.get_sensor retrieves a sensor value.
        # BP.PORT_1 specifies that we are looking for the value of sensor port 1.
        # BP.get_sensor returns the sensor value (what we want to display).
        try:
            alue = BP.get_sensor(BP.PORT_1)
            blue = BP.get_sensor(BP.PORT_2)
            clue = BP.get_sensor(BP.PORT_3)
            dlue = BP.get_sensor(BP.PORT_4)
            print(alue,blue,clue,dlue)                         # print the distance in CM
        except brickpi3.SensorError as error:
            print(error)
        if alue + dlue >= 36 and blue+clue <= 20:
            print('r')
        elif alue+dlue<= 20 and blue+clue >= 36:
            print('l')
        elif alue+blue>=28 and alue+blue<=60:
            print('r')
        elif clue+dlue>=28 and clue+dlue<=60:
            print('l')
        else:
            print('f')
            
        
        time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()  