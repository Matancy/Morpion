import pygame
def cross(display, cords):
    if cords[0] == 0 and cords[1] == 0:
        pygame.draw.line(display, (0, 0, 0), (100, 100), (200, 200), 2)
        pygame.draw.line(display, (0, 0, 0), (200, 100), (100, 200), 2)
    elif cords[0] == 1 and cords[1] == 0:
        pygame.draw.line(display, (0, 0, 0), (400, 100), (500, 200), 2)
        pygame.draw.line(display, (0, 0, 0), (500, 100), (400, 200), 2)
    elif cords[0] == 2 and cords[1] == 0:
        pygame.draw.line(display, (0, 0, 0), (700, 100), (800, 200), 2)
        pygame.draw.line(display, (0, 0, 0), (800, 100), (700, 200), 2)
    elif cords[0] == 0 and cords[1] == 1:
        pygame.draw.line(display, (0, 0, 0), (100, 400), (200, 500), 2)
        pygame.draw.line(display, (0, 0, 0), (200, 400), (100, 500), 2)
    elif cords[0] == 1 and cords[1] == 1:
        pygame.draw.line(display, (0, 0, 0), (400, 400), (500, 500), 2)
        pygame.draw.line(display, (0, 0, 0), (500, 400), (400, 500), 2)
    elif cords[0] == 2 and cords[1] == 1:
        pygame.draw.line(display, (0, 0, 0), (700, 400), (800, 500), 2)
        pygame.draw.line(display, (0, 0, 0), (800, 400), (700, 500), 2)
    elif cords[0] == 0 and cords[1] == 2:
        pygame.draw.line(display, (0, 0, 0), (100, 700), (200, 800), 2)
        pygame.draw.line(display, (0, 0, 0), (200, 700), (100, 800), 2)
    elif cords[0] == 1 and cords[1] == 2:
        pygame.draw.line(display, (0, 0, 0), (400, 700), (500, 800), 2)
        pygame.draw.line(display, (0, 0, 0), (500, 700), (400, 800), 2)
    elif cords[0] == 2 and cords[1] == 2:
        pygame.draw.line(display, (0, 0, 0), (700, 700), (800, 800), 2)
        pygame.draw.line(display, (0, 0, 0), (800, 700), (700, 800), 2)
    pygame.display.flip()