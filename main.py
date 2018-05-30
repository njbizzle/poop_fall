import pygame


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

x = 0
y = 0
yVelocity=0
gravity=00.05

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

    y+=yVelocity

    if  x>510:
        x=0

    if y>400:
        y=0
  #      yVelocity=0

    if keyDown (pygame.K_d):
        x += 1
    if keyDown(pygame.K_w):
        y -= 10
    if keyDown(pygame.K_a):
        x -= 1


    #draw
    screen.fill(WHITE)

    #pygame.draw.circle(screen, RED,(int(x), 20), 50)
    screen.blit(poop, (int(x), int(y)))




    pygame.display.flip()