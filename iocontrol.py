import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)

#Button one - GPS/IMU on
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Button 2 - Beep sound
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#LED GPS and IMU data collection
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
    gps  = GPIO.input(22)
    beep = GPIO.input(27)
    led  = GPIO.input(17)
    if beep == True:
        subprocess.call("python3 /home/pi/Documents/mobilemapping/main.py", shell=True)
    if gps == True:
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        time.sleep(5)
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    time.sleep(0.2)
