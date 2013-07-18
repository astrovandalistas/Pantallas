#!/bin/bash

# start Pantalla(tgh)
export DISPLAY=":0.0"
startx &
python pantalla_tgh.py --inport=7878 --localnetport=8989 --localnet=aeffect04.local --inip=aeffect04.local
