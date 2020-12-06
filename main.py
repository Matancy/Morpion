import pygame
from function.display import *
from function.drawing import *
from function.calculs import *

display = pygame.display.set_mode((900, 900))

# Variables
started = 0
#

run = True
while run:
    # Lecture des évènements de Pygame
    for event in pygame.event.get():
        # Fermeture du programme
        if event.type == pygame.QUIT:
            run = False

        # Lecture des entrées clavier
        if event.type == pygame.KEYDOWN:
            # Touche entrée
            if event.key == pygame.K_RETURN:
                started = 1

        # Lecture des entrées souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Clic gauche
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pos = pygame.mouse.get_pos()
                if started == 1:
                    print(calcul_pos(pos[0], pos[1]))


    if started == 0:
        load_screen(display)
        pygame.display.flip()
    else:
        paint_grid(display)
        pygame.display.flip()
pygame.quit()