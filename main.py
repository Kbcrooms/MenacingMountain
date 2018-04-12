import pygame, time
#from player import *
from player import Player
from platform import Platform
from snowpea import Snowpea
from speedbar import Speedbar
screenWidth = 640
screenHeight = 480
framerate = 60
prevSpeedTime = [time.clock()]
background = pygame.image.load('background.png')
pygame.init()
clock = pygame.time.Clock()
#screen = pygame.display.set_mode((screenWidth,screenHeight),pygame.FULLSCREEN)
screen = pygame.display.set_mode((screenWidth,screenHeight))
screen.fill((255,255,255))
screen.blit(background, (0, 0))
running = True
speed = [0]
entities = []
platforms = []
hazards = []
widgets = []
speedbar = Speedbar(screen,speed)
platform = Platform(screen,0,370,640,130)
platform2 = Platform(screen,720,370,640,130)
platforms.append(platform)
platforms.append(platform2)
snowpea = Snowpea(screen, 380, 325, platforms)
hazards.append(snowpea)
player = Player(screen, (255,0,0),120,350,platforms,hazards)
#player is always at entity 0 index
entities.append(player)
entities.append(snowpea)
entities.append(platform)
entities.append(platform2)
widgets.append(speedbar)


def draw():
    for entity in entities:
        entity.draw()
    for widget in widgets:
        widget.draw()

def update():
    #need check to determine if platform still exists
    #prob need to change to for number loop
    for entity in entities:
        entity.update()

    for widget in widgets:
        widget.update()
def move():
    if(speed[0]>9):
        speed[0] = 9
    if(speed[0]>0):
        if(time.clock()-prevSpeedTime[0]>.1):
            speed[0]-=1
            prevSpeedTime[0] = time.clock()
        for i in range(1,len(entities)):
            entities[i].move(speed[0])

while running:
    delta = clock.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print ("right")
                if(player.onPlatform()):
                    speed[0] += 3
                    prevSpeedTime[0] = time.clock()
            elif event.key == pygame.K_DOWN:
                print ("down")
            elif event.key == pygame.K_SPACE:
                print ("jump")
                player.jump()
            elif event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.KEYUP:
            print ("Key Up")
    screen.blit(background, (0, 0))
    update()
    draw()
    move()
    pygame.display.flip()
