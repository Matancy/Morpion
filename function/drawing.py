import pygame


def circle(display, cords):
    if cords[0] == 0 and cords[1] == 0:
        pygame.draw.circle(display, (0, 0, 0), (150, 150), 100, 2)
        pygame.display.flip()