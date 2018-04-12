import pygame
class Platform(object):

    def __init__(self,screen,posx,posy,width,height,platforms,entities):
        self.screen = screen
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.avi = pygame.draw.rect(self.screen,(25,255,255),(self.posx,self.posy,self.width,self.height),0)
        self.platforms = platforms
        self.entities = entities
        self.wasOnscreen = 0

    def draw(self):
        self.avi = pygame.draw.rect(self.screen,(165, 242, 243),(self.posx,self.posy,self.width,self.height),0)

    def update(self):
        if self.offscreenleft():
            self.platforms.remove(self)
            self.entities.remove(self)
            #generatelevel()
        return

    def move(self,movedist):
        self.posx -= movedist

    def offscreenleft(self):
        return (self.posx + self.width < 0)
