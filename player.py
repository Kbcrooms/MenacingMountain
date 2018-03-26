import pygame
class Player(object):

    def __init__(self,screen,color):
        self.color = color
        self.screen = screen
    def draw(self):
        pygame.draw.circle(self.screen,self.color,(310,230,20),1)
