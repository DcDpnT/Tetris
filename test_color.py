import pygame

try:
    color = pygame.Color('darkorange')
except ValueError:
    print("La couleur 'darkorange' n'est pas disponible dans Pygame.")
else:
    print("La couleur 'darkorange' est disponible dans Pygame.")
