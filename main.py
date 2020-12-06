import pygame
#from function.display import *

display = pygame.display.set_mode((900, 900))

run = True
while run:
    img = pygame.image.load("data/start.jpg")
    display.blit(img, (0, 0))
    pygame.display.flip()
pygame.quit()