import pygame
class Speedbar(object):

    def __init__(self,screen,speed):
        self.screen = screen
        self.posx = 500
        self.posy = 450
        self.color = (130,130,130)
        self.speedmarkers = []
        self.radius = 5
        self.speed = speed
        for i in range(0,9):
            self.speedmarkers.append(pygame.draw.circle(self.screen,self.color,(self.posx + i*10 ,self.posy),self.radius,1))
    def draw(self):
        for i in range(0,9):
            if i<= self.speed[0]:
                self.speedmarkers[i] = pygame.draw.circle(self.screen,self.color,(self.posx + i*10 ,self.posy),self.radius,0)
            else:
                self.speedmarkers[i] = pygame.draw.circle(self.screen,self.color,(self.posx + i*10 ,self.posy),self.radius,1)



    def update(self):
        return
