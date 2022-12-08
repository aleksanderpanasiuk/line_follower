from ev3dev.ev3 import *
from time import sleep

cl = ColorSensor()

cl.mode = "COL-REFLECT"

while True:
    print(cl.value())
    sleep(0.5)
