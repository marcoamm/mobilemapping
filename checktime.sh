#!/bin/bash

while true;
do

    pps=$(ntpq -p | grep PPS | awk {'print $5'})
    gps=$(ntpq -p | grep GPS | awk {'print $5'})
    

    if [ "${pps}" -lt 8 -a "${gps}" -lt 64  ]
    then
        echo "I have time" | ts '[%Y-%M-%D %H:%m:%.S]' > log.txt
	python3 blink.py
	break
    fi
    sleep 2s
done

