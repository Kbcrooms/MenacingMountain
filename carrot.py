import pygame, time, math
from player import Player


class Carrot(pygame.sprite.Sprite):

    def __init__(self,x,y,player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.width = 30
        self.height = 10
        self.x = x
        self.y = y
        self.images = []
        self.images.append(pygame.image.load('sprites/projectiles/carrot/carrot_1.png'))
        self.images.append(pygame.image.load('sprites/projectiles/carrot/carrot_2.png'))
        self.angle = round(math.degrees(math.atan((player.y-self.y)/(self.x-player.x))))
        print (self.angle)
        self.image = pygame.transform.rotate(pygame.transform.scale(self.images[0],(self.width,self.height)),self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        self.prevMoveTime = time.clock()
        self.prevAniTime = time.clock()
        self.animateCount = 0


    def update(self):
        if(time.clock()-self.prevAniTime >.1):
            self.animateCount += 1
            self.image = pygame.transform.rotate(pygame.transform.scale(self.images[self.animateCount%2],(self.width,self.height)),self.angle)
            self.prevAniTime = time.clock()

        if(time.clock()-self.prevMoveTime >.02):
            self.rect.x += 10/math.tan(self.angle)
            self.rect.y -= 10*math.tan(self.angle)
            self.prevMoveTime = time.clock()
        if pygame.sprite.collide_rect(self,self.player):
            print ("Life lost")
            self.player.hurt()
            self.kill()
