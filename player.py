import pygame
class Player(object):

    def __init__(self,screen,color,posx,posy,platforms,hazards):
        self.color = color
        self.screen = screen
        self.posx = 100
        self.posy = 150
        self.platforms = platforms
        self.hazards = hazards
        self.last_posx = 0
        self.last_posy = 0
        self.width = 35
        self.height = 55
        self.avi = pygame.draw.rect(self.screen,self.color,(self.posx,self.posy,self.width,self.height),0)
        self.jumpCounter = -1
        self.alive = True

    def draw(self):
        self.avi = pygame.draw.rect(self.screen,self.color,(self.posx,self.posy,self.width,self.height),0)

    def update(self):
        self.deathcheck()
        if (not self.alive):
            self.color = (255,0,0)


        if self.jumpCounter >-1:
            self.jumpCounter+=1
            if self.jumpCounter<16:
                self.posy-=10

            else:
                self.jumpCounter = -1
        else:
            if(not self.onPlatform()):
                self.posy+=6




    def jump(self):
        if(self.onPlatform()):
            self.jumpCounter = 0

    def onPlatform(self):
        for platform in self.platforms:
            if (platform.posx<=self.posx and platform.posx+platform.width>=self.posx or platform.posx+platform.width>=self.posx+self.width and platform.posx<=self.posx+self.width ):
                return platform.avi.colliderect(self.avi)

    def deathcheck(self):
        if not self.screen.get_rect().contains(self.avi):
            self.alive = False
        for hazard in self.hazards:
            if(hazard.avi.colliderect(self.avi)):
                self.alive = False
