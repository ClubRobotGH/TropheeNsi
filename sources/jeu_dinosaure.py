import pygame
import time
from random import *
import fonctions
pygame.init()

pygame.mixer.init()

info = pygame.display.Info()
width = int(info.current_w * 1)
height = int(info.current_h * 1)

screen = pygame.display.set_mode((width,height))

vague_fond = pygame.image.load("../data/vague_fond.jpg")
vague_fond = pygame.transform.scale(vague_fond, (width, height))
sprite = pygame.image.load("../data/poisson.png")
sprite = pygame.transform.scale(sprite, (height//8, height//8))



font = pygame.font.Font(None, 50)
text_color = (0, 0, 0)



def jeu():

    fin = False
    clock = pygame.time.Clock()
    keys = pygame.key.get_pressed()

    #obstacle
    lenght_obstacle = width // 5
    height_obstacle = height // 4
    x_obstacle = 0
    y_obstacle = height //1.50
    bateau = pygame.image.load("../data/bateau.png")


    #sprite
    x_sprite = width*6//8
    y_sprite = (height * 6) // 8


    #game mechanics

    #jumping
    jumping = False
    force = 10

    score = 0

    #obstacle speed
    vitesse = 5

    while not fin:

        bateau = pygame.transform.scale(bateau, (lenght_obstacle, 200))

        endX_obstacle = x_obstacle + lenght_obstacle
        endY_obstacle = y_obstacle

        endX_sprite = x_sprite
        endY_sprite = y_sprite + (height // 8)

        text = font.render(str(score), True, text_color)
        screen.blit(vague_fond, (0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin = True
                fonctions.leaving()

            if event.type == pygame.KEYDOWN:  # When a key is pressed

                if event.key == pygame.K_UP and not jumping:
                    jumping = True

        #le sprite saute
        if jumping:
            force -= 0.1
            y_sprite -= force
            screen.blit(sprite,(x_sprite,y_sprite))

        #si le sprite atteint son point de depart
        if y_sprite >= (height * 6) // 8:
            jumping = False
            y_sprite = height * 6 // 8
            force = 10
            screen.blit(sprite,(x_sprite,y_sprite))

        #si le sprite touche l'obstacle
        if endX_obstacle > endX_sprite and endY_obstacle < endY_sprite and x_obstacle < x_sprite:
            fin = True

        x_obstacle += vitesse

        screen.blit(bateau,(x_obstacle,y_obstacle))
        if x_obstacle >= width:
            x_obstacle = 0
            lenght_obstacle = randint(300, 700)
            score += 1
            vitesse += 0.2
            screen.blit(bateau,(x_obstacle,y_obstacle))

        clock.tick(60)

        pygame.display.flip()






