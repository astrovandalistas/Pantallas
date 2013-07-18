# -*- coding: utf-8 -*-

import sys, time, subprocess, pygame, getopt
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

    def loop(self):
        self._checkEvent()
        ## check state
        if (not self.messageQ.empty()):
            (locale,type,txt) = self.messageQ.get()
            txt = txt.replace('\0','')
            words = txt.split()
            lasrgestWord = max(txt.split(),key=len)
            for (index,w) in enumerate(words):
                self._checkEvent()
                bgndC = (0,0,0) if(index%2 or w == lasrgestWord) else (255,255,255)
                textC = (128,0,0) if (w == lasrgestWord) else((255,255,255) if index%2 else (0,0,0))
                self._fadeTextInOut(w,bgndC,textC)
                index += 1

    def _checkEvent(self):
        for event in pygame.event.get():
            if ((event.type == pygame.QUIT) or
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                raise KeyboardInterrupt

    def _fadeTextInOut(self,txt,bgndColor=(0,0,0),textColor=(255,255,255)):
        alpha = 1
        alphaD = 64
        dispTime = 0
        (FADEIN,FADEOUT,DISPLAY) = range(3)
        currState = FADEIN

        mSurface = self.font.render(txt+" ", 1, textColor, bgndColor)
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
            self.background.fill(bgndColor)
            self.background.blit(mSurface, mRect)
            self.screen.blit(self.background, (0,0))
            pygame.display.flip()

if __name__=="__main__":
    (inIp, inPort, localNetAddress, localNetPort) = ("127.0.0.1", 7878, "127.0.0.1", 8989)
    opts, args = getopt.getopt(sys.argv[1:],"i:p:n:o:",["inip=", "inport=","localnet=","localnetport="])
    for opt, arg in opts:
        if(opt in ("--inip","-i")):
            inIp = str(arg)
        elif(opt in ("--inport","-p")):
            inPort = int(arg)
        elif(opt in ("--localnet","-n")):
            localNetAddress = str(arg)
        elif(opt in ("--localnetport","-o")):
            localNetPort = int(arg)

    mAST = Pantalla(inIp, inPort, localNetAddress, localNetPort)
    runPrototype(mAST)
