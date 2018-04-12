import pygame, time
#from player import *
from player import Player
from platform import Platform
from snowpea import Snowpea
from speedbar import Speedbar
screenWidth = 640
screenHeight = 480
framerate = 60
key=[0]
key[0] = "MenMon"
prevSpeedTime = [time.clock()]
background = pygame.image.load('background_small.png')
pygame.init()
font = pygame.font.SysFont("Helvetica", 25)
score = [0]
scorecard = [0]
scorecard[0] = font.render(str(score[0]), True, (0, 0, 0))
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
speedbar = Speedbar(screen,speed)
platform = Platform(screen,0,460,640,20,platforms,entities)
platform2 = Platform(screen,720,460,640,20,platforms,entities)
platforms.append(platform)
platforms.append(platform2)
snowpea = Snowpea(screen, 380, 400, platforms)
widgets = []
hazards.append(snowpea)
player = Player(screen, (255,0,0),120,350,platforms,hazards)
#player is always at entity 0 index
entities.append(player)
entities.append(snowpea)
entities.append(platform)
entities.append(platform2)
widgets.append(speedbar)


def generatelevel():
    value = hash(key[0])
    print(value)

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
        if(time.clock()-prevSpeedTime[0]>.3):
            speed[0]-=1
            prevSpeedTime[0] = time.clock()
        for i in range(1,len(entities)):
            entities[i].move(speed[0])
        score[0]+= speed[0]
        scorecard[0] = font.render(str(score[0]), True, (255, 255, 255))

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
    screen.blit(scorecard[0],(10,0))

    update()
    draw()
    move()
    for platform in platforms:
        print(screen.get_rect().contains(platform.avi))
    print(len(platforms))
    pygame.display.flip()
