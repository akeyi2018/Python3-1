from gpiozero import Motor
from time import sleep

motor = Motor(19,26)
motor2 = Motor(6,13)

motor.forward()
motor2.forward()
sleep(3)
        