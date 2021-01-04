import pygame
from function.drawing import *
from function.calculs import *
from function.save import *


def init():
    display.fill((255, 255, 255))
    pygame.draw.line(display, (0, 0, 0), (0, 100), (300, 100), 2)
    pygame.draw.line(display, (0, 0, 0), (0, 200), (300, 200), 2)
    pygame.draw.line(display, (0, 0, 0), (100, 0), (100, 300), 2)
    pygame.draw.line(display, (0, 0, 0), (200, 0), (200, 300), 2)
    pygame.display.flip()
    global player_count, game_data, game_finished
    player_count, game_data, game_finished = 0, [0, 0, 0, 0, 0, 0, 0, 0, 0], 0

display = pygame.display.set_mode((300, 300))
init()

run = True
while run:
    # Lecture des évènements de Pygame
    for event in pygame.event.get():
        # Fermeture du programme
        if event.type == pygame.QUIT:
            run = False

        # Touche entrée
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            init()

        # Lecture des entrées souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                # Si la partie n'est pas finie
                if game_finished == 0:
                    player_count += 1
                    if player(player_count) == "cross":
                        position = calcul_pos(pos[0], pos[1])
                        if save_cords(game_data, position, 1):
                            cross(display, position)
                            if is_winner(game_data):
                                print("Gagnant : Croix\n Press ENTER to restart")
                                game_finished = 1
                        else:
                            player_count -= 1
                    elif player(player_count) == "circle":
                        if save_cords(game_data, position, 2):
                            circle(display, position)
                            if is_winner(game_data):
                                print("Gagnant : Cercle\n Press ENTER to restart")
                                game_finished = 1
                            else:
                                player_count -= 1
                        if player_count == 9 and game_finished != 1:
                            print("Perdu !\n Press ENTER to restart")
                            game_finished = 1

pygame.quit()