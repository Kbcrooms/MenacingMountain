import pygame
#from player import *
from player import Player
pygame.init()
screen = pygame.display.set_mode((640,480))
screen.fill((255,255,255))
running = True
entities = []
player = Player(screen, (255,0,0))
entities.append(player)

def update():
    for entity in entities:
        entity.draw()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        update()
    pygame.display.flip()
