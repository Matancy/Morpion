import pygame

def load_screen(display):
    img = pygame.image.load("data/start.jpg")
    display.blit(img, (0, 0))