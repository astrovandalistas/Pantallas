#importa python time
import time
#importa pygame module
import pygame


class Click:

    x = .5 # izquierda = 0, derecha = 1, centro = .5
    speed = 0 # distancia por segundo

    def __init__(self):
        self._previous_update = time.time()
        self._previous_sound = time.time()
        self._channel = pygame.mixer.Channel(0)
        # guarda archivo de audio en la memoria
        self._sound = pygame.mixer.Sound("dash.wav")

    def update(self):
        # actualiza las coordinadas 
        self.x += (time.time() - self._previous_update) * self.speed
        if self.x > 1:
            self.x = 1
        elif self.x < 0:
            self.x = 0
        self._previous_update = time.time()

    def render(self):
        # genera un sonido cada .1 seconds (if moving) or .5 seconds (if still)
        interval = .1 if self.speed else .5
        if time.time() >= self._previous_sound + interval:
            # apaga el sonido
            self._channel.stop()
            self._channel.play(self._sound)
            self._channel.set_volume(1 - self.x, self.x)
            self._previous_sound = time.time()


# inicia pygame
pygame.init()

# display (parece que el event loop la requiere para correr)
pygame.display.set_mode((320, 200))

# crea el objeto click
click = Click()

# loop forever (hasta que break ocurra)
while True:
    # get event desde el event queue
    for event in pygame.event.get():
        # eventos temporalmente de keyboard (remplazar pro eventos de pantalla)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                click.speed = -.2
            elif event.key == pygame.K_RIGHT:
                click.speed = .2
            #  "escape" key...
            elif event.unicode == "q" or event.key == pygame.K_ESCAPE:
                # ... sale del while loop
                # (break no funciona con un for loop )
                raise SystemExit
        # cuando los keys son liberados...
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                click.speed = 0
    # actualiza a click
    click.update()
    # render click (como audio)
    click.render()
    # do nothing 
    # (para evitar  CPU al 100%)s
    time.sleep(.001)
