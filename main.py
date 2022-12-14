from ev3dev.ev3 import *
from time import sleep

cl = ColorSensor()
cl.mode = "COL-REFLECT"

motor_R = LargeMotor("outA")
motor_L = LargeMotor("outB")

# 80 - 52s
# 75 - 55s
# 66 - 60s
# 50 - 76s

speed = 80

while True:
    color_value = cl.value()
    print(color_value)

    if color_value < 9:
        motor_R.run_forever(speed_sp = -speed)
        motor_L.run_forever(speed_sp = speed)

    elif  9 < color_value <= 15:
        motor_R.run_forever(speed_sp = -speed)
        motor_L.run_forever(speed_sp = 0)

    elif 39 <= color_value <= 45:
        motor_L.run_forever(speed_sp = -speed)
        motor_R.run_forever(speed_sp = 0)

    elif 45 < color_value:
        motor_L.run_forever(speed_sp = -speed)
        motor_R.run_forever(speed_sp = speed)

    else:
        motor_L.run_forever(speed_sp = -speed)
        motor_R.run_forever(speed_sp = -speed)

