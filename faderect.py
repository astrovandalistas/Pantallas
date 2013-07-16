import pygame
from pygame.locals import *

pygame.init()
 
FPS = 30
fpsClock = pygame.time.Clock()
 
screen = pygame.display.set_mode((1280,800))
shape = screen.convert_alpha()
 
alpha = 1
WHITE = (255, 255, 255,alpha)
BLACK = (0,0,0)
 
stimulus = pygame.Rect(500,250,500,500)
 
def fade():
    global alpha
    alpha = alpha + 5 
    
    if alpha >= 255:
        alpha = -255
    screen.fill(BLACK)
    shape.fill(BLACK)
    pygame.draw.rect(shape,(255, 255, 255,abs(alpha)),stimulus)
    screen.blit(shape,(0,0))
    pygame.display.update(stimulus)
    fpsClock.tick(FPS)
 
while alpha!=0:
    fade() 
