#!/bin/bash

#Wait 3 minutes before starting
sleep 30s

#Kills all processes logging data that are running
pkill -f str2str

#Goes to home folder
#cd ~

#Obtaining the time of the output
collect_time=$(date +%y-%m-%d-%H-%M-%S)

#Reads devices plugged in the USB ports
for sysdevpath in $(find /sys/bus/usb/devices/usb*/ -name dev); do
    (
        syspath="${sysdevpath%/dev}"
        devname="$(udevadm info -q name -p $syspath)"
        [[ "$devname" == "bus/"* ]] && continue
        eval "$(udevadm info -q property --export -p $syspath)"
        [[ -z "$ID_SERIAL" ]] && continue
        echo "/dev/$devname - $ID_SERIAL"
        case $ID_SERIAL in
            Prolific_Technology_Inc._USB-Serial_Controller_D)
                nohup ./str2str -in serial://${devname}:115200:8:none:none#stq -out file://${collect_time}-gps${devname:-1}.stq &
                ;;
            1a86_USB2.0-Serial)
                nohup ./str2str -in serial://${devname}:115200:8:none:none# -out file://${collect_time}-imu.nmea &        
                ;;
            *)
                echo .
                ;;
        esac
    )
done
