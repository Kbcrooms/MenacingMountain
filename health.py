import pygame, time

class Health(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.width = 20
        self.height = 20
        self.image = pygame.transform.scale(pygame.image.load('sprites/coffee/coffee.png'),(self.width,self.height))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)


    def update(self):
        return
