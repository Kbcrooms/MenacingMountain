import pygame
class Player(object):

    def __init__(self,screen,color,posx,posy,platforms):
        self.color = color
        self.screen = screen
        self.posx = 120
        self.posy = 351
        self.platforms = platforms
        self.last_posx = 0
        self.last_posy = 0
        self.width = 20
        self.height = 20
        self.avi = pygame.draw.rect(self.screen,self.color,(self.posx,self.posy,self.width,self.height),0)
        self.jumpCounter = -1

    def draw(self):
        self.avi = pygame.draw.rect(self.screen,self.color,(self.posx,self.posy,20,20),0)

    def update(self):
        if self.jumpCounter >-1:
            self.jumpCounter+=1
            if self.jumpCounter<10:
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
            if (platform.posx<=self.posx and platform.posx+platform.width>=self.posx):
                return platform.avi.colliderect(self.avi)
