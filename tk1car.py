import time

import GPIOWrapper as GPIO

#GPIO Pin number of the Car
FORWARD = 57
BACK = 164
LEFT = 165
RIGHT = 166

#Method which move the car in a direction during t seconds
def move(t, direction):
    print "About to turn %d" % direction
    GPIO.activate(direction)
    time.sleep(t)
    GPIO.reset(direction)

#Method which init the GPIO pin
def init_mouvement():
    GPIO.init(FORWARD)
    GPIO.init(LEFT)
    GPIO.init(RIGHT)
    GPIO.init(BACK)

#Method which reset the GPIOs and release them
def close_mouvement():
    GPIO.reset(FORWARD)
    GPIO.reset(BACK)
    GPIO.reset(RIGHT)
    GPIO.reset(LEFT)
    GPIO.release(FORWARD)
    GPIO.release(BACK)
    GPIO.release(RIGHT)
    GPIO.release(LEFT)

#Method ro go forward during t seconds
def forward(t):
	#we activate forward
    GPIO.activate_time(FORWARD, t + 0.2)
    #we activate back in order to slow the car
    GPIO.activate_time(BACK, 0.5)
    GPIO.reset(FORWARD)
    GPIO.reset(BACK)

#Method to go back during t seconds
def backward(t):
	#we activate back
    GPIO.activate_time(BACK, t + 0.2)
    #we activate forward in order to slow the car
    GPIO.activate_time(FORWARD, 0.5)
    GPIO.reset(FORWARD)
    GPIO.reset(BACK)

#Method to turn in a direction (RIGHT or LEFT)
def turn45(direction,t):
    GPIO.activate(direction)
    GPIO.activate_time(FORWARD, t + 0.2)
    GPIO.activate_time(BACK,0.5)

    GPIO.reset(FORWARD)
    GPIO.reset(BACK)
    GPIO.reset(direction)

#Method to turn back in a direction (RIGHT or LEFT)
def turnBack45(direction, t):
    GPIO.activate(direction)
    GPIO.activate_time(BACK, t + 0.2)
    GPIO.activate_time(FORWARD,0.5)
    GPIO.reset(direction)
    GPIO.reset(FORWARD)
    GPIO.reset(BACK)
