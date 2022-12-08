from ev3dev.ev3 import *
from time import sleep

motor_R = LargeMotor("outA")
motor_L = LargeMotor("outB")

motor_R.run_timed(time_sp=1000, speed_sp=-1000)
motor_L.run_timed(time_sp=1000, speed_sp=-1000)

sleep(3)
