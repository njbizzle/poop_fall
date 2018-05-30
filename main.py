import pygame
import random

keys={}

#hberbhirebihebuile

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (255,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)


def keyDown(key):
    if key in  keys:
        return  keys[key]
    else:
        return False


pygame.init()

screen = pygame.display.set_mode((510,510))

drawLoop = True
clock = pygame.time.Clock()
poop=pygame.image.load("Poop_Emoji.png")
fireball=pygame.image.load("Fireball.png")

fbxVal=10
fbx = 560
fby = random.randint(100,400)
x = 0
y = 0
grounded=False
yVelocity=0
gravity=1

while drawLoop == True:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawLoop=False
        if event.type == pygame.KEYDOWN:
            keys[event.key] = True
        if event.type == pygame.KEYUP:
            keys[event.key] = False



    #update
    clock.tick(60)
    yVelocity+=gravity
    fbx-=fbxVal
    y+=yVelocity
    if  x>560:
        x=-100
    if  x<-100:
        x=560
    if y>400:
        y=400
    if fbx < -100:
        fbx = 560
        fby = random.randint(100, 400)
        grounded=True

    if keyDown (pygame.K_d):
        x += 5
    if keyDown(pygame.K_w) and grounded==True:
        yVelocity=-30
        grounded=False
    if keyDown(pygame.K_a):
        x -= 5


    #draw
    screen.fill(WHITE)

    #pygame.draw.circle(screen, RED,(int(x), 20), 50)
    screen.blit(poop, (int(x), int(y)))
    screen.blit(fireball, (int(fbx), int(fby)))




    pygame.display.flip()