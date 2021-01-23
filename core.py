import sys, pygame
from pygame.locals import *
from assets.classes.textview import *
from assets.styles.default import *
from game import *

pygame.init()

#global constants
fps = int(1000/60)
size = width, height = 640, 480
pygame.display.set_caption('Snake Game')

#global variables
speed = [0, 0]
#pygame.mouse.set_visible(0)
screen = pygame.display.set_mode(size)

#textviews
textviews = {
    'start' : Textview(70, 100, Default.tv_spacing_small, "Start", Default.tv_style_secondary),
    'exit' : Textview(70, 150, Default.tv_spacing_small, "Exit", Default.tv_style_secondary)
}

#functions
def exit():
    pygame.quit()
    sys.exit()

#image = pygame.image.load("assets/images/pc.jpg")
#imagerect = image.get_rect()
#rect0 = Rect(200, 200, 50, 80)

while 1:
    #get all pressed keys
    pressedKeys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        mousePos = pygame.mouse.get_pos()
        for name, textview in textviews.items():
            if textview.getRect().collidepoint(mousePos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    textview.click()
                    if name=="exit":
                        exit()
                    elif name=="start":
                        r = game(pygame, screen, exit)
                        print(r)
                else:
                    textview.hover()
            else:
                textview.default()

    if pressedKeys != None:
        if pressedKeys[pygame.K_w]: speed[1] = -1
        if pressedKeys[pygame.K_a]: speed[0] = -1
        if pressedKeys[pygame.K_s]: speed[1] = +1
        if pressedKeys[pygame.K_d]: speed[0] = +1

    #rect0 = rect0.move(speed)
    speed = [0, 0]
    
    #if imagerect.left < 0 or imagerect.right > width:
    #    speed[0] = -speed[0]
    #if imagerect.top < 0 or imagerect.bottom > height:
    #    speed[1] = -speed[1]

    #screen.blit(image, imagerect)
    screen.fill(Default.menu_bg_color)

    #draw textviews
    [textviews[name].draw(screen) for name in textviews]

    #pygame.draw.rect(screen, black, rect0)
    pygame.display.flip()
    pygame.time.delay(fps)
