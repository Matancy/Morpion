import pygame

run = True
while run:
    display = pygame.display.set_mode((900, 900))
    img = pygame.image.load("data/start.jpg")
    display.blit(img, (0, 0))
    pygame.display.flip()
pygame.quit()