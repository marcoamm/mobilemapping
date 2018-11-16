#!/bin/bash

pps=$(ntpq -p | grep PPS | awk {'print $5'})
gps=$(ntpq -p | grep GPS | awk {'print $5'})


if [ "${pps}" -lt 8 -a "${gps}" -lt 64  ]
then
    echo "I have time" > ~/log.txt
fi

