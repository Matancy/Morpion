#Importation des fonctions

import pygame
from function.display import *

#display()
display = pygame.display.set_mode((900, 900))
# Variables
#started = 0
#

#run = True
#while run:
  #if started == 0:
    ##load_screen(display)
    #pygame.display.flip()
  
img = pygame.image.load("data/start.jpg")
display.blit(img, (30, 150))

