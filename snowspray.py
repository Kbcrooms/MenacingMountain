import pygame, time

class Snowspray(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.visible = 1
        self.width = 110
        self.height = 110
        self.images = []
        self.images.append(pygame.image.load('sprites/snowspray/snowspray_1.png'))
        self.images.append(pygame.image.load('sprites/snowspray/snowspray_2.png'))
        self.images.append(pygame.image.load('sprites/snowspray/snowspray_3.png'))
        self.images.append(pygame.image.load('sprites/snowspray/snowspray_4.png'))
        self.image = pygame.transform.scale(self.images[0],(self.width,self.height))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        self.prevTime = time.clock()
        self.animateCount = 0

    def update(self):
        if(time.clock()-self.prevTime >.1):
            self.prevTime = time.clock()
            self.animateCount += 1
            self.image = pygame.transform.scale(self.images[self.animateCount%4],(self.width,self.height*self.visible))
