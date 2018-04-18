import pygame, time, os, math
from player import Player
from snowman import Snowman
from snowspray import Snowspray
from carrot import Carrot
from health import Health

screenWidth = 640
screenHeight = 480
framerate = 60
background = pygame.image.load('background.png')
snowSprites = []
snowSprites.append(pygame.image.load('sprites/snow/snow_1.png'))
snowSprites.append(pygame.image.load('sprites/snow/snow_2.png'))
snowSprites.append(pygame.image.load('sprites/snow/snow_3.png'))
snowSprites.append(pygame.image.load('sprites/snow/snow_4.png'))
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('sounds/soundtrack.wav')
#pygame.mixer.music.play(-1)
font = pygame.font.SysFont("Helvetica", 25)
startmenu = font.render('Press Enter to Start', True, (255, 255, 255))
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Menacing Mountain")
screen.fill((255,255,255))
screen.blit(background, (0, 0))
clock = pygame.time.Clock()
prevTime = time.clock()
slopeY = 480-(math.tan(20)/640)
mountainSprite = pygame.draw.polygon(screen,(255,255,255),((0,350),(0,slopeY),(800,480)))
animateCount = 0
sprites = pygame.sprite.Group()
healthbarX = 20
healthbarY = 460
healthbar = [Health(healthbarX,healthbarY),Health(healthbarX+20,healthbarY),Health(healthbarX+40,healthbarY)]
snowspray= Snowspray(120,355)
player= Player(150,370,healthbar,snowspray)
snowman = Snowman(520,100)
carrot = Carrot(320,240,player,mountainSprite)
carrot2 = Carrot(520,100,player,mountainSprite,320,480)
sprites.add(player)
sprites.add(snowman)
sprites.add(snowspray)
sprites.add(carrot)
sprites.add(carrot2)
sprites.add(healthbar)
running = True
playing = False
while running:
    delta = clock.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.setJump()
            elif event.key == pygame.K_RIGHT:
                player.setDash()
            elif event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                playing = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.jumping = False
            elif event.key == pygame.K_RIGHT:
                player.dashing = False
        elif event.type == pygame.QUIT:
            running = False
    if playing:
        #Update Start
        sprites.update()
        #Update End

        #Draw Start
        screen.blit(background, (0, 0))
        mountainSprite = pygame.draw.polygon(screen,(255,255,255),((0,350),(0,slopeY),(800,480)))
        sprites.draw(screen)
        screen.blit(snowSprites[animateCount%4],(0,0))
        if(time.clock()-prevTime>.035):
            animateCount += 1
            prevTime = time.clock()
        #Draw End
    elif not playing:
        screen.fill((0,0,0))
        screen.blit(startmenu,startmenu.get_rect(center=(320,240)))
    if player.lives<=0:
        playing = False
        player.reset()
        healthbar = [Health(healthbarX,healthbarY),Health(healthbarX+20,healthbarY),Health(healthbarX+40,healthbarY)]
        sprites.add(healthbar)
        animateCount = 0
        #prob need more varibales reset
    pygame.display.flip()
