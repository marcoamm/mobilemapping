import RPi.GPIO as GPIO
import subprocess
import os
from time import sleep

GPIO.setmode(GPIO.BCM)

#Button one - GPS/IMU on
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Button 2 - Beep sound
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#LED GPS and IMU data collection
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Aux variable
gpsswitch = 0

while True:
    gps  = GPIO.input(22)
    beep = GPIO.input(27)
    if beep == True:
        subprocess.call("python3 /home/pi/Documents/mobilemapping/main.py", shell=True)
    if gps == True:
        subprocess.call("nohup /home/pi/Documents/mobilemapping/read_imu_gps.sh | ts '[%Y-%m-%d %H:%M:%.S]' > log.txt &", shell=True)
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        sleep(2)
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        gpsswitch = 1
    if gpsswitch == 1:    
        file1 = os.stat('/home/pi/Documents/mobilemapping/log.txt')
        f1s = file1.st_size
        sleep(10)
        file2 = os.stat('/home/pi/Documents/mobilemapping/log.txt')
        f2s = file2.st_size
        diff = f2s - f1s
        if diff == 0:
            subprocess.call("echo 'Logging stopped' | ts '[%Y-%m-%d %H:%M:%.S]' > log.txt &", shell=True)
            GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            gpsswitch = 0
        else:
            GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    sleep(0.2)



