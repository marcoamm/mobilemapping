import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#REd LED of death
for i in range(10):
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    sleep(0.5)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    sleep(0.5)
