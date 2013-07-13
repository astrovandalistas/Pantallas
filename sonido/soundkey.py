import pygame
pygame.init()
sound = pygame.mixer.Sound("TR-909Kick.wav")
pygame.display.set_mode((320, 200))

while True:
  event = pygame.event.wait()
  if event.type == pygame.KEYDOWN:
      sound.play()
      if event.unicode == "q" or event.key == pygame.K_ESCAPE:
          break