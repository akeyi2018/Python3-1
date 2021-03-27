from time import sleep
from gpiozero import PWMOutputDevice

pinList = [19,26,6,13]

forward = [1,0,1,0]
back = [0,1,0,1]
turnLeft = [0,1,0,0]
turnRight = [0,0,0,1]
stop = [0,0,0,0]

forwardLeft = PWMOutputDevice(19, True, 0, 60)
reverseLeft = PWMOutputDevice(26, True, 0, 60)
 
forwardRight = PWMOutputDevice(6, True, 0, 60)
reverseRight = PWMOutputDevice(13, True, 0, 60)
 
def allStop():
	forwardLeft.value = 0
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 0
 
def forwardDrive():
	forwardLeft.value = 1.0
	reverseLeft.value = 0
	forwardRight.value = 1.0
	reverseRight.value = 0
 
def reverseDrive():
	forwardLeft.value = 0
	reverseLeft.value = 1.0
	forwardRight.value = 0
	reverseRight.value = 1.0
def forwardTurnLeft():
	forwardLeft.value = 0.0
	reverseLeft.value = 1.0
	forwardRight.value = 0.0
	reverseRight.value = 0
 
def forwardTurnRight():
	forwardLeft.value = 0.0
	reverseLeft.value = 0.0
	forwardRight.value = 0.0
	reverseRight.value = 1.0


forwardDrive()
sleep(1)
reverseDrive()
sleep(1)
allStop()
