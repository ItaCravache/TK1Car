import time as t

import GPIOWrapper as GPIO

import tk1car as car

"""
Test cases for the GPIOWrapper
"""

#GPIO pin number
forw = 57
right = 166
left = 165
back = 164

#Initialisation of the GPIO
GPIO.init(forw)
GPIO.init(left)
GPIO.init(back)
GPIO.init(right)

i=0
print("go")

#Go forward during 1sec, then go back during another 1sec
GPIO.activate_time(forw,1)
GPIO.activate_time(back,1)

#Turn right and left
while i<5:
	GPIO.activate_time(right,0.2)
	GPIO.activate_time(left,0.2)
	i=i+1
	print(i)
	
#Release the GPIO
GPIO.release(right)
GPIO.release(forw) 
GPIO.release(left)
GPIO.release(back)
print("stop")

