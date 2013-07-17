#carga un sonido 
import time

import pygame
pygame.init()

sound = pygame.mixer.Sound("dash.wav")

#canales
channel = sound.play()
channel.set_volume(1, 0)
time.sleep(1)

channel = sound.play()
channel.set_volume(0, 1)
time.sleep(1)

channel = sound.play()
channel.set_volume(1, 1)
time.sleep(1)