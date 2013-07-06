# -*- coding: utf-8 -*-

#!/usr/bin/env python

import pygame

pygame.init()
x = 260
y = 260
dx = 45
dy = 45
# crear una pantalla
screen = pygame.display.set_mode((400, 400))

# texto a mostrar
font = pygame.font.Font(None, 66)
text = font.render("Disruptivo", True, (100, 100, 100))

display = True

# loon principa;
while pygame.time.get_ticks() < 10000: # corre el programa por 10 segundo
     # bora la pantalla
     screen.fill((255, 255, 255))

     display = not display

     # dibuja el texto en la pantalla si display es True
     if display:
         screen.blit(text, (100, 100))

     # update screen
     pygame.display.flip()

     # espera medio segundo
     pygame.time.wait(500)
     

stop = False
def add_visible_ty():
     if stop: return
     message = games.Message(
         value = "eso es",
         size = 100,
         color = color.red,
         x = games.screen.width/2,
         y = games.screen.height/2,
         lifetime = 500,
         after_death = add_invisible_ty
     )
     games.screen.add(message)

def add_invisible_ty():
     if stop: return
     message = games.Message(
         value = "upsss",
         size = 100,
         color = color.red,
         x = games.screen.width/2,
         y = games.screen.height/2,
         lifetime = 500,
         after_death = add_visible_ty
     )
     games.screen.add(message)