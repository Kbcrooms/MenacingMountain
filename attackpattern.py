import pygame, time, random
from carrot import Carrot

class AttackPattern():

    def __init__(self,player,sprites,projectiles):
        self.player = player
        self.sprites = sprites
        self.projectiles = projectiles
        self.prevTime = time.time()
        self.cooldown = 2 #seconds
    def attack(self,score):
        if(time.time()-self.prevTime>self.cooldown):
            if(score<250):
                self.attack1()
            elif(score<500):
                self.attack2(200,370)
                self.attack1()
            else:
                if(score%2):
                    self.cooldown=1.25
                    self.attack1()
                    self.attack3(540,80)
                else:
                    self.cooldown=2.25
                    self.attack2(200,370)
                    self.attack1()
            self.prevTime = time.time()
    def reset(self):
        cooldown = 1

    #Simple shot at Players curent location
    def attack1(self):
        carrot = Carrot(520,100,self.player,self.player.x+((random.randint(0,3))*25),self.player.y)
        self.sprites.add(carrot)
        self.projectiles.add(carrot)


    #Shot at specified ground position
    def attack2(self,x,y):
        carrot = Carrot(520,100,self.player,x+((random.randint(0,3))*25),y)
        self.sprites.add(carrot)
        self.projectiles.add(carrot)

    def attack3(self,startx,starty):
        carrot = Carrot(startx,starty,self.player,self.player.x+((random.randint(0,3))*25),self.player.y)
        self.sprites.add(carrot)
        self.projectiles.add(carrot)
