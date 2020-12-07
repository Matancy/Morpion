import pygame


def circle(display, cords):
    if cords[0] == 0 and cords[1] == 0:
        pygame.draw.circle(display, (0, 0, 0), (150, 150), 100, 2)
        pygame.display.flip()
    elif cords[0] == 1 and cords[1] == 0:
        pygame.draw.circle(display, (0, 0, 0), (450, 150), 100, 2)
        pygame.display.flip()
    elif cords[0] == 2 and cords[1] == 0:
        pygame.draw.circle(display, (0, 0, 0), (750, 150), 100, 2)
        pygame.display.flip()
    elif cords[0] == 0 and cords[1] == 1:
        pygame.draw.circle(display, (0, 0, 0), (150, 450), 100, 2)
        pygame.display.flip()
    elif cords[0] == 1 and cords[1] == 1:
        pygame.draw.circle(display, (0, 0, 0), (450, 450), 100, 2)
        pygame.display.flip()
    elif cords[0] == 2 and cords[1] == 1:
        pygame.draw.circle(display, (0, 0, 0), (750, 450), 100, 2)
        pygame.display.flip()
    elif cords[0] == 0 and cords[1] == 2:
        pygame.draw.circle(display, (0, 0, 0), (150, 750), 100, 2)
        pygame.display.flip()
    elif cords[0] == 1 and cords[1] == 2:
        pygame.draw.circle(display, (0, 0, 0), (450, 750), 100, 2)
        pygame.display.flip()
    elif cords[0] == 2 and cords[1] == 2:
        pygame.draw.circle(display, (0, 0, 0), (750, 750), 100, 2)


def cross(display, cords):
    if cords[0] == 0 and cords[1] == 0:
        pygame.draw.line(display, (0, 0, 0), (100, 100), (200,200), 2)
        pygame.draw.line(display, (0, 0, 0), (200, 100), (100, 200), 2)
        pygame.display.flip()