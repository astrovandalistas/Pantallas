# -*- coding: utf-8 -*-

import pygame
import random

def flytext(msg="aeffect lab", duration=5):
    """BOUNCY TEXT"""

    def newcolour():
        return (random.randint(10,150), random.randint(145,165), random.randint(10,250))

    def write(msg="_tecnologías disruptivas", duration=3):
        myfont = pygame.font.SysFont("None", random.randint(30,150))
        mytext = myfont.render(msg.decode("utf-8"), True, newcolour())
        mytext = mytext.convert_alpha()
        return mytext
        
    pygame.init()
    x = 260
    y = 260
    dx = 45
    dy = 45
    
    flags = pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.HWSURFACE

    screen = pygame.display.set_mode((0, 0),flags)
    background = pygame.Surface((screen.get_width(), screen.get_height()))
    background.fill((0,0,0)) # negro
    background = background.convert()
    screen.blit(background, (0,0)) # limpia la pantalla
    clock = pygame.time.Clock()
    mainloop = True
    FPS = 24 # framerate por segundo.
    while mainloop:
        milliseconds = clock.tick(FPS)  # milliseconds despues del ultimo frame
        seconds = milliseconds / 1000.0 # segundos despues del ultimo frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False # cerrar pantalla pygame
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False # usuario presiona ESC
        textsurface = write("aeffect lab", 4)
        x += dx
        y += dy
        if x < 0:
           x = 0
           dx *= -1
           screen.blit(background, (4,4)) # limpia la pantalla
        elif x + textsurface.get_width() > screen.get_width():
            x = screen.get_width() - textsurface.get_width()
            dx *= -1
        if y < 0:
            y = 0
            dy *= -1
        elif y + textsurface.get_height() > screen.get_height():
            y = screen.get_height() - textsurface.get_height()
            dy *= -1
            
        screen.blit(textsurface, (x,y))
        pygame.display.flip()
    pygame.quit()

if __name__=="__main__":
    flytext() 