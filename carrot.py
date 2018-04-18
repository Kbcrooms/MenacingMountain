import pygame, time, math
from player import Player


class Carrot(pygame.sprite.Sprite):

    def __init__(self,x,y,player,mountainSprite,*attackLock):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.mountain = mountainSprite
        self.width = 30
        self.height = 10
        self.speed = 7
        self.x = x
        self.y = y
        self.images = []
        self.images.append(pygame.image.load('sprites/projectiles/carrot/carrot_1.png'))
        self.images.append(pygame.image.load('sprites/projectiles/carrot/carrot_2.png'))
        self.attackLock = [0,0]
        if len(attackLock)==2:
            self.attackLock[0] = attackLock[0]
            self.attackLock[1] = attackLock[1]
        else:
            self.attackLock[0]=self.player.x
            self.attackLock[1]=self.player.y
        self.ratio = (self.y - self.attackLock[1])/(self.x - self.attackLock[0])
        self.angle = round(math.degrees(-1*math.atan(self.ratio)))
        self.image = pygame.transform.rotate(pygame.transform.scale(self.images[0],(self.width,self.height)),self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        self.prevMoveTime = time.clock()
        self.prevAniTime = time.clock()
        self.animateCount = 0


    def update(self):
        if(time.clock()-self.prevAniTime >.1):
            self.ratio = (self.y - self.attackLock[1])/(self.x - self.attackLock[0])
            self.animateCount += 1
            self.image = pygame.transform.rotate(pygame.transform.scale(self.images[self.animateCount%2],(self.width,self.height)),self.angle)
            self.prevAniTime = time.clock()

        if(time.clock()-self.prevMoveTime >.02):
            self.x += round(self.speed/self.ratio)
            self.y -= round(self.speed*self.ratio)
            self.rect.center = (self.x,self.y)
            self.prevMoveTime = time.clock()
        if pygame.sprite.collide_rect(self,self.player):
            self.player.hurt()
            self.kill()
        if self.y>480 or self.y<0 or self.x>640 or self.x<0:
            self.kill()
