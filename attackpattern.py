import pygame, time, random
from carrot import Carrot

class AttackPattern():

    def __init__(self,player,sprites):
        self.player = player
        self.sprites = sprites
        self.prevTime = time.clock()
        self.cooldown = 2 #seconds
    def attack(self,score):
        if(time.clock()-self.prevTime>self.cooldown):
            if(score<250):
                self.attack1()
            elif(score<500):
                self.attack2(200,370)
                self.attack1()
            else:
                self.attack1()
                self.attack3(540,80)
            self.prevTime = time.clock()
    def reset():
        return

    #Simple shot at Players curent location
    def attack1(self):
        self.sprites.add(Carrot(520,100,self.player,self.player.x+((random.randint(0,3))*25),self.player.y))

    #Shot at specified ground position
    def attack2(self,x,y):
        self.sprites.add(Carrot(520,100,self.player,x+((random.randint(0,3))*25),y))

    def attack3(self,startx,starty):
        self.sprites.add(Carrot(startx,starty,self.player,self.player.x+((random.randint(0,3))*25),self.player.y))
