import pygame, time, math
from snowspray import Snowspray


class Player(pygame.sprite.Sprite):

    def __init__(self,x,y,healthbar,snowspray):
        pygame.sprite.Sprite.__init__(self)
        self.snowspray = snowspray
        self.healthbar = healthbar
        self.width = 75
        self.height = 60
        self.images = []
        self.images.append(pygame.image.load('sprites/girl/girl_1.png'))
        self.images.append(pygame.image.load('sprites/girl/girl_2.png'))
        self.images.append(pygame.image.load('sprites/girl/girl_3.png'))
        self.images.append(pygame.image.load('sprites/girl/girl_4.png'))
        self.image = pygame.transform.scale(self.images[0],(self.width,self.height))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        self.prevTime = time.time()
        self.animateCount = 0
        self.lives = 3
        self.jumping = 0
        self.jumpTime = 0
        self.jumpSpeed = 5
        self.jumpSound = pygame.mixer.Sound('sounds/jump_woosh.wav')
        self.dashing = 0
        self.dashTime = 0
        self.dashSpeed = 4

    def update(self):
        if(time.time()-self.prevTime >.1):
            self.prevTime = time.time()
            self.animateCount += 1
            self.image = pygame.transform.scale(self.images[self.animateCount%4],(self.width,self.height))
        if (self.jumping and time.time()-self.jumpTime<.45):
            self.y -= 2*self.jumpSpeed
            self.rect.center = (self.x,self.y)

        elif((not self.jumping or time.time()-self.jumpTime>=.45)and self.y < 370):
            self.y += self.jumpSpeed
            self.rect.center = (self.x,self.y)
        self.snowspray.visible = self.y >= 370 and self.x <= 150

        if (self.dashing and time.time()-self.dashTime<.6):
            self.y += self.dashSpeed
            self.x += self.dashSpeed
            self.rect.center = (self.x,self.y)

        elif((not self.jumping or time.time()-self.dashTime>=.6)and self.x > 150):
            self.y -= self.dashSpeed
            self.x -= self.dashSpeed
            self.rect.center = (self.x,self.y)


    def hurt(self):
        self.lives-=1
        self.healthbar[self.lives].kill()


    def reset(self,healthbar):
        self.lives = 3
        self.healthbar = healthbar

    def setJump(self):
        if(self.y >= 370):
            self.jumpSound.play()
            self.jumpTime = time.time()
            self.jumping = 1

    def setDash(self):
        if(self.x <= 150):
            self.jumpSound.play()
            self.dashTime = time.time()
            self.dashing = 1
