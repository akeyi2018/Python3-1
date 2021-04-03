from gpiozero import Motor
from time import sleep

motor = Motor(19,26)

motor.forward()
sleep(3)

        