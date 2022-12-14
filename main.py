from ev3dev.ev3 import *
from time import sleep

cl = ColorSensor()
cl.mode = "COL-REFLECT"

motor_R = LargeMotor("outA")
motor_L = LargeMotor("outB")

while True:
    color_value = cl.value()
    print(color_value)

    if color_value < 9:
        motor_R.run_forever(speed_sp = -50)
        motor_L.run_forever(speed_sp = 50)

    elif  9 < color_value <= 15:
        motor_R.run_forever(speed_sp = -50)
        motor_L.run_forever(speed_sp = 0)

    elif 39 <= color_value <= 45:
        motor_L.run_forever(speed_sp = -50)
        motor_R.run_forever(speed_sp = 0)

    elif 45 < color_value:
        motor_L.run_forever(speed_sp = -50)
        motor_R.run_forever(speed_sp = 50)

    else:
        motor_L.run_forever(speed_sp=-100)
        motor_R.run_forever(speed_sp=-100)
