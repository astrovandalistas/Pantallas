# -*- coding: utf-8 -*-

import sys, time, subprocess, pygame
sys.path.append("../LocalNet")
from interfaces import PrototypeInterface, runPrototype

class Pantalla(PrototypeInterface):
    """ Pantalla prototype class
        all prototypes must define setup() and loop() functions
        self.messageQ will have all messages coming in from LocalNet """

    def setup(self):
        ## subscribe to all receivers
        self.subscribeToAll()
        flags = pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.HWSURFACE
        ##flags = 0

        pygame.init()
        self.screen = pygame.display.set_mode((0, 0),flags)
        pygame.display.set_caption('aeffectLab')
        pygame.mouse.set_visible(False)

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))

        self.font = pygame.font.Font("./arial.ttf", 800)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        s = "Aeffect Lab es un framework para facilitar la creación de modelos afectivos de comunicación".decode('utf-8')
        self.messageQ.put(("t","t",s))

    def _fadeTextInOut(self,txt):
        alpha = 1
        alphaD = 64
        dispTime = 0
        (FADEIN,FADEOUT,DISPLAY) = range(3)
        currState = FADEIN

        mSurface = self.font.render(txt+" ", 1, (255,255,255), (0,0,0))
        mRect = mSurface.get_rect()
        scale = min(float(self.background.get_width())/mRect.width, float(mRect.width)/self.background.get_width())
        mSurface = pygame.transform.scale(mSurface,(int(scale*mRect.width),int(scale*mRect.height)))
        mRect = mSurface.get_rect(centerx=self.background.get_width()/2,
                                  centery=self.background.get_height()/2)

        while(alpha > 0):
            if(currState is FADEIN):
                alpha+=alphaD
                if(alpha>255):
                    dispTime = time.time()
                    alpha = 255
                    currState = DISPLAY
            elif(currState is DISPLAY):
                if(time.time()-dispTime > 0.2):
                    currState = FADEOUT
            elif(currState is FADEOUT):
                alpha -= alphaD

            mSurface.set_alpha(alpha)
            self.background.fill((0,0,0))
            self.background.blit(mSurface, mRect)
            self.screen.blit(self.background, (0,0))
            pygame.display.flip()


    def loop(self):
        ## handle events
        for event in pygame.event.get():
            if ((event.type == pygame.QUIT) or
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                raise KeyboardInterrupt

        ## check state
        if (not self.messageQ.empty()):
            (locale,type,txt) = self.messageQ.get()
            words = txt.split()
            for w in words:
                self._fadeTextInOut(w)

if __name__=="__main__":
    ## TODO: get ip and ports from command line
    mAST = Pantalla(6666,"127.0.0.1",7777)
    runPrototype(mAST)
