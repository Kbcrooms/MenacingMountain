import pygame
class Player(object):

    def __init__(self,screen,color):
        self.color = color
        self.screen = screen
        self.posx = 120
        self.posy = 350
        self.last_posx = 0
        self.last_posy = 0
        self.avi = pygame.draw.rect(self.screen,self.color,(self.posx,self.posy,20,20),0)
        self.jumpCounter = -1
    def draw(self):
        self.avi = pygame.draw.rect(self.screen,self.color,(self.posx,self.posy,20,20),0)
    def update(self):
        if self.jumpCounter >-1:
            self.jumpCounter+=1
            if self.jumpCounter<10:
                self.posy-=10
            elif self.jumpCounter>=29:
                self.jumpCounter = -1
            elif self.jumpCounter>10:
                self.posy+=5


    def jump(self):
        self.jumpCounter = 0
