import pygame
class Snowpea(object):

    def __init__(self,screen,posx,posy,platforms):
        self.screen = screen
        self.color = (153,149,83)
        self.posx = posx
        self.posy = posy
        self.width = 25
        self.height = 45
        self.sprite = pygame.image.load("snowman.png")
        self.avi = pygame.Rect(self.posx,self.posy,self.width,self.height)
    def draw(self):
        #self.avi = pygame.draw.rect(self.screen,self.color,(self.posx,self.posy,self.width,self.height),0)
        self.screen.blit(self.sprite,(self.posx,self.posy))
    def update(self):
        self.avi = pygame.Rect(self.posx,self.posy,self.width,self.height)
        return

    def move(self,movedist):
        self.posx -= movedist
#use seeds to generte levels and save high score for each seed
