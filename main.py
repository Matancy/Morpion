import pygame
from function.display import *
from function.drawing import *
from function.calculs import *
from function.save import *

# Mise en place du plateau de jeu
display = pygame.display.set_mode((900, 900))

# Variables
started = 0
player_count = 0
game_data = [0,0,0,0,0,0,0,0,0]
game_finished = 0
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
                if started == 2:
                    if game_finished == 0:
                        player_count += 1
                        if player(player_count) == "cross":
                            position = calcul_pos(pos[0], pos[1])
                            if save_cords(game_data, position, 1):
                                cross(display, position)
                                if is_winner(game_data):
                                    print("Gagnant : Croix")
                                    game_finished = 1
                            else:
                                player_count -= 1
                        else:
                            position = calcul_pos(pos[0], pos[1])
                            if save_cords(game_data, position, 2):
                                circle(display, position)
                                if is_winner(game_data):
                                    print("Gagnant : Cercle")
                                    game_finished = 1
                            else:
                                player_count -= 1


    if started == 0:
        load_screen(display)
        pygame.display.flip()
    elif started == 1:
        paint_grid(display)
        pygame.display.flip()
        started += 1

pygame.quit()