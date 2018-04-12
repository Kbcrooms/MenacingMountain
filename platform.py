import pygame
class Platform(object):

    def __init__(self,screen,posx,posy,width,height):
        self.screen = screen
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.avi = pygame.draw.rect(self.screen,(25,255,255),(self.posx,self.posy,self.width,self.height),0)

    def draw(self):
        self.avi = pygame.draw.rect(self.screen,(25,255,255),(self.posx,self.posy,self.width,self.height),0)

    def update(self):
        return

    def move(self,movedist):
        self.posx -= movedist
