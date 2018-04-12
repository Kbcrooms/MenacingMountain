import pygame
class Snowpea(object):

    def __init__(self,screen,posx,posy,platforms):
        self.screen = screen
        self.color = (153,149,83)
        self.posx = posx
        self.posy = posy
        self.width = 25
        self.height = 45
        self.avi = pygame.draw.rect(self.screen,self.color,(self.posx,self.posy,self.width,self.height),0)
    def draw(self):
        self.avi = pygame.draw.rect(self.screen,self.color,(self.posx,self.posy,self.width,self.height),0)

    def update(self):
        return

    def move(self,movedist):
        self.posx -= movedist
