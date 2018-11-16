import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)

#Button one - GPS/IMU on
GPIO.setup(22, GPIOIN, pull_up_down=GPIO.PUD_UP)

#Button 2 - Beep sound
GPIO.setup(27, GPIOIN, pull_up_down=GPIO.PUD_UP)

#LED GPS and IMU data collection
GPIO.setup(17, GPIOIN, pull_up_down=GPIO.PUD_UP)


while True:
    gps  = GPIO.input(22)
    beep = GPIO.input(27)
    led  = GPIO.input(17)
    if beep == False:
        subprocess.call("python3 /home/pi/mobilemapping/main.py", shell=True)
    time.sleep(0.2)