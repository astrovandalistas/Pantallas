## molaa
isrun=`ps -u tgh | grep python | wc -l`
if [ $isrun -lt 1 ] 
then 
    cd /home/pi/Dev/Pantallas
    export DISPLAY=":0.0"
    startx &
    while [ 1 -le 20 ]
    do
	python pantallaserver.py --inport=8989 --localnetport=8900 --localnet=aeffect07.local --inip=aeffect04.local &
	killpid0=$!
	sleep 2
	python pantalla_tgh.py --inport=7878 --localnetport=8989 --localnet=aeffect04.local --inip=aeffect04.local &
	killpid1=$!
	sleep 100
	kill -9 $killpid0
	kill -9 $killpid1
    done
fi

