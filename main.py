import pygame
from function.display import *
from function.events import *

display = pygame.display.set_mode((900, 900))

# Variables
started = 0
#

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                started = 1
    if started == 0:
        load_screen(display)
        pygame.display.flip()
    else:
        display.fill((0, 0, 0))
        pygame.display.flip()
pygame.quit()