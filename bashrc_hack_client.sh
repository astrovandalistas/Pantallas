# molaa
isrun=`ps -u tgh | grep python | wc -l`
if [ $isrun -lt 1 ] 
then 
    cd /home/pi/Dev/Pantallas
    sleep 20
    export DISPLAY=":0.0"
    startx &
    while [ 1 -le 20 ]
    do
	python pantalla_tgh.py --inport=7878 --localnetport=8989 --localnet=aeffect04.local --inip=aeffect05.local &
	killpid=$!
	sleep 100
	kill -9 $killpid
    done
fi

