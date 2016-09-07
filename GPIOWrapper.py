import time

# Path and value constants
BASE_PATH = '/sys/class/gpio'

EXPORT_PATH = BASE_PATH + '/export'
UNEXPORT_PATH = BASE_PATH + '/unexport'

GPIO_PATH = BASE_PATH + '/gpio%d'
GPIO_DIRECTION_PATH = GPIO_PATH + '/direction'
GPIO_VALUE_PATH = GPIO_PATH + '/value'

HIGH = '1'
LOW = '0'

INPUT = 'in'
OUTPUT = 'out'


def init(pin, direction='out'):
    """
    Initializes a certain pin by setting its output
    @type pin: int
    @param pin: the pin number
    """
    with open(EXPORT_PATH, 'w') as ex:
        ex.write('%d' % pin)

    with open(GPIO_DIRECTION_PATH % (pin), 'w') as dir:
        dir.write(direction)


# Set the pin to HIGH
def activate(pin):
    """
    @type pin: int
    @param pin: the pin number
    """
    with open(GPIO_VALUE_PATH % (pin), 'w') as dir:
        dir.write(HIGH)


# Set the pin to HIGH for a limited time
def activate_time(pin, t):
    """
    @type pin: int
    @param pin: the pin number
    @type t: int
    @param t: time how long the pin will be activated
    """
    with open(GPIO_VALUE_PATH % (pin), 'w') as dir:
        dir.write(HIGH)

    time.sleep(t)

    with open(GPIO_VALUE_PATH % (pin), 'w') as dir:
        dir.write(LOW)


# Reset the pin to LOW
def reset(pin):
    """
    @type pin: int
    @param pin: the pin number
    """
    with open(GPIO_VALUE_PATH % (pin), 'w') as dir:
        dir.write(LOW)


# Release the pin
def release(pin):
    """
    @type pin: int
    @param pin: the pin number
    """
    with open(UNEXPORT_PATH, 'w') as ex:
        ex.write('%d' % pin)

# Get the value of the pin
def value(pin):
    return int(open(GPIO_VALUE_PATH % (pin),'r').read())



	
