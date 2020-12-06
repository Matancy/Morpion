import pygame
from function.display import *

display = pygame.display.set_mode((900, 900))

run = True
while run:
    load_screen(display)
    pygame.display.flip()
pygame.quit()