import pygame


def exit_game(run, event):
    if event.type == pygame.QUIT:
        run = False
    return run

def test(event):
    if event.type == pygame.K_SPACE:
        print("ok")