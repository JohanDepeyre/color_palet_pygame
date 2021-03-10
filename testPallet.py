import pygame
from pygame.locals import *


pygame.init()
fenetre = pygame.display.set_mode((1200, 600))


#add image
fond = pygame.image.load("palet.png").convert()
#show image
fenetre.blit(fond, (0, 0))

while True:
    # Rafraichissement


    for event in pygame.event.get():  # wait event
    #click event
        if event.type == MOUSEBUTTONDOWN:
            coordinates = pygame.mouse.get_pos()

            # mouse_position is in the form [x,y], we only want the x part
            x = coordinates[0]
            y = coordinates[1]
            #get RGBA color in x,y position
            color = fond.get_at((x, y))
            #draw line with de color selected
            pygame.draw.line(fenetre, color , (5,500), (500,500), 50)
                
  
  
    pygame.display.flip()
