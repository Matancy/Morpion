import pygame

# Création de l'espace de travail

def display():
  display = pygame.display.set_mode((900, 900))


#Fonction d'affichage de l'écran de démarrage

def load_screen(display):
  img = pygame.image.load("data/start.jpg")
  display.blit(img, (30, 150))
