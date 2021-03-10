import pygame
from pygame.locals import *


pygame.init()
fenetre = pygame.display.set_mode((1200, 600))





# Chargement et collage du fond
fond = pygame.image.load("test.png").convert()
fenetre.blit(fond, (0, 0))

while True:
    # Rafraichissement


    for event in pygame.event.get():  # Attente des événements
        if event.type == MOUSEBUTTONDOWN:
            coordinates = pygame.mouse.get_pos()

            # mouse_position is in the form [x,y], we only want the x part
            x = coordinates[0]
            y = coordinates[1]

            print(fond.get_at((x, y)))
            pygame.draw.line(fenetre, fond.get_at((x, y)) , (5,500), (500,500), 50)
                
  
  
    pygame.display.flip()
