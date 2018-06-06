import pygame
import random

keys={}



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
fireball2=pygame.image.load("Fireball.png")
fbxVal2=10
fbxVal=10
fbx = 560
fby = random.randint(100,400)
x = 0
y = 0
fbx2=0
fby2=0
end=True
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
    fbx2-=fbxVal2-5
    fbx-=fbxVal-3
    y+=yVelocity
    if  x>560:
        x=-100
    if  x<-100:
        x=560
    if y>400:
        y=400
        grounded = True
    else:
        grounded = False
    if fbx < -100:
        fbx = 560
        fby = random.randint(100, 400)
    if fbx2 < -100:
        fbx2 = 560
        fby2 = y
    if fby and fbx == y and y or fby2 and fbx2 == y and y:
        while end==True:
            fby=0
            fbx=0
            fbx2=0
            fby2=0
            y=0
            x=0

    if keyDown (pygame.K_d):
        x += 5
    if keyDown(pygame.K_w) and grounded==True:
        yVelocity=-20
    if keyDown(pygame.K_a):
        x -= 5


    #draw
    screen.fill(WHITE)

    #pygame.draw.circle(screen, RED,(int(x), 20), 50)
    screen.blit(poop, (int(x), int(y)))
    screen.blit(fireball, (int(fbx), int(fby)))
    screen.blit(fireball2, (int(fbx2), int(fby2)))

    pygame.display.flip()
