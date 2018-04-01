import pygame
class Enemy(object)

    def __init__(self,screen):
        self.screen = screen
        self.color = (0,0,255)
        self.posx = 640
        self.posy = 350
        self.avi = pygame.draw.rect(self.screen,self.color,(self.posx,self.posy,30,30),0)
    def draw(self):
        self.avi = pygame.draw.rect(self.screen,self.color,(self.posx,self.posy,30,30),0)
    def update(self,distance):
        self.posx-=distance
