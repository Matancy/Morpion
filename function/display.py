import pygame


def load_screen(display):
    img = pygame.image.load("data/start.jpg")
    display.blit(img, (0, 0))

def paint_grid(display):
    display.fill((255, 255, 255))
    pygame.draw.line(display, (0, 0, 0), (0, 300), (900, 300), 2)
    pygame.draw.line(display, (0, 0, 0), (0, 600), (900, 600), 2)
    pygame.draw.line(display, (0, 0, 0), (300, 0), (300, 900), 2)
    pygame.draw.line(display, (0, 0, 0), (600, 0), (600, 900), 2)