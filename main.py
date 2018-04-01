import pygame, time
#from player import *
from player import Player
screenWidth = 640
screenHeight = 480
framerate = 60
background = pygame.image.load('background.png')
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screenWidth,screenHeight))
screen.fill((255,255,255))
screen.blit(background, (0, 0))
running = True
speed = 0
entities = []
player = Player(screen, (255,0,0))
entities.append(player)

def draw():
    for entity in entities:
        entity.draw()

def update():
    for entity in entities:
        entity.update()
def move():
    for i in range(1,len(entities)):
        entities[i].move()
while running:
    delta = clock.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print ("right")
                move()
            elif event.key == pygame.K_SPACE:
                print ("jump")
                player.jump()
        elif event.type == pygame.KEYUP:
            print ("Key Up")
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen,(25,255,255),(0,370,640,130),0)
    update()
    draw()
    pygame.display.flip()
