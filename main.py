import pygame, time, os, math
from player import Player
from snowman import Snowman
from snowspray import Snowspray
from carrot import Carrot
from health import Health
from attackpattern import AttackPattern
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
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.mixer.init()
pygame.mixer.music.load('sounds/soundtrack.wav')
pygame.mixer.music.play(-1)
font = pygame.font.SysFont("Helvetica", 45)
font.set_bold(True)
startmenu = font.render('Menacing Mountain', True, (128, 0, 0))
startMenuBody  = pygame.Rect(0, 0, 520,60)
startMenuBody.center=(320,180)
font.set_bold(False)
highscore = 0
buttonFont = font.render("Start", True, (255, 255, 255))
buttonBody = pygame.Rect(0, 0, 240,60)
buttonBody.center=(320,360)
font = pygame.font.SysFont("Helvetica", 25)
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
#carrot = Carrot(320,240,player)
#carrot2 = Carrot(520,100,player,320,480)
sprites.add(player)
sprites.add(snowman)
sprites.add(snowspray)
#sprites.add(carrot)
#sprites.add(carrot2)
sprites.add(healthbar)
running = True
playing = False
attackpattern = AttackPattern(player,sprites)
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
                pygame.mixer.music.stop()
                pygame.mixer.music.play(-1)
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
        attackpattern.attack(animateCount)
        scoreboard = font.render(str(animateCount), True, (128, 80, 0))
        #Update End

        #Draw Start
        screen.blit(background, (0, 0))
        mountainSprite = pygame.draw.polygon(screen,(255,255,255),((0,350),(0,slopeY),(800,480)))
        sprites.draw(screen)
        screen.blit(snowSprites[animateCount%4],(0,0))
        screen.blit(scoreboard,scoreboard.get_rect(center=(320,460)))
        if(time.clock()-prevTime>.035):
            animateCount += 1
            prevTime = time.clock()
        #Draw End
    elif not playing:
        mouse = pygame.mouse.get_pos()

        screen.fill((0,0,0))
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (128,128,128), startMenuBody)
        screen.blit(startmenu,startmenu.get_rect(center=(320,180)))

        if 320+120 > mouse[0] > 320-120 and 360+30 > mouse[1] > 360-30:
            pygame.draw.rect(screen, (172,0,0), buttonBody)
            if pygame.mouse.get_pressed()[0]:
                playing = True
        else:
            pygame.draw.rect(screen, (128,0,0), buttonBody)

        if highscore>0:
            buttonFont = font.render("Retry", True, (255, 255, 255))
            font.set_bold(True)
            highscoreFont = font.render("Highscore: "+str(highscore), True, (255,215,0))
            font.set_bold(False)
            screen.blit(highscoreFont,highscoreFont.get_rect(center=(320,270)))

        screen.blit(buttonFont,buttonFont.get_rect(center=(320,360)))



    if player.lives<=0:
        playing = False
        healthbar = [Health(healthbarX,healthbarY),Health(healthbarX+20,healthbarY),Health(healthbarX+40,healthbarY)]
        player.reset(healthbar)
        sprites.add(healthbar)
        if(animateCount>highscore):
            highscore = animateCount
        animateCount = 0
        #prob need more varibales reset
    pygame.display.flip()
