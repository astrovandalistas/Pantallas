# -*- coding: utf-8 -*-


import sys,os, pygame
pygame.init()

alpha = 0
BLACK = (0,0,0)
GREEN = (0,255,0, alpha)
BLUE = (255, 80, 5, alpha)
WHITE = (255,255,255, alpha)
TAN = (210, 180, 140) 
SIZE = 1200, 900 


INTRO_TEXT = ['Somos un colectivo translocal',
 'que se enfoca en el desarrollo de',
 'proyectos que conjuntan investigacion,',
 'accion artistica, tecnologia y activismo,',
 'bajo la logica del hacking urbano',
 'y la divulgacion libre del conocimiento.',]
 
flags = pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.HWSURFACE
screen = pygame.display.set_mode((0, 0),flags)
pygame.mouse.set_visible(False)
  
def initializeFont(string,pos1,pos2,pos3,pos4,color):
         if pygame.font:
              verdana = pygame.font.match_font('Verdana')
              font = pygame.font.Font(verdana,50)
              text = font.render(string,1,color)
              textpos = pygame.Rect(pos1,pos2,pos3,pos4)
              pygame.display.get_surface().blit(text,textpos)
              

def displayText(textList):
      pos1 = 50
      pos2 = 150
      pos3 = 50
      pos4 = 50
      pygame.display.get_surface().fill(BLACK)
      for string in textList:
               initializeFont(string,pos1,pos2,pos3,pos4,TAN)
               pos2 += 55
               pygame.display.update()
               textEventLoop()
               
def textEventLoop():
    mainClock = pygame.time.Clock()
    time_elapsed = 0
    while True:
        time_elapsed = time_elapsed + mainClock.tick(60)
        if time_elapsed > 1600:
             return
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                   pygame.quit()
             elif event.type == pygame.KEYDOWN:
                   return
                  
                  
                
                
displayText(INTRO_TEXT)