import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pinList = [19,26,6,13]

forward = [1,0,1,0]
back = [0,1,0,1]
turnLeft = [0,1,0,0]
turnRight = [0,0,0,1]
stop = [0,0,0,0]

#���X�g�^�ɂ��GPIO�s���̐ݒ�
GPIO.setup(pinList, GPIO.OUT)

#direct->�����̔z��Gtm->�^�q���ԕb
def FunMoveMotor(direct: list, tm: int):
    
	#Zip���g�p���邱�Ƃɂ��]����肩�Ȃ�Z���v���O�������쐬���邱�Ƃ��\�ɂȂ�
	for pin, val in zip(pinList, direct):
        GPIO.output(pin, val)

    sleep(tm)


FunMoveMotor(forward, 1)

FunMoveMotor(stop, 0.5)

GPIO.cleanup

print("Finish")
