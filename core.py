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

    screen.fill(Default.menu_bg_color)

    #draw textviews
    [textviews[name].draw(screen) for name in textviews]

    pygame.display.flip()
    pygame.time.delay(fps)
