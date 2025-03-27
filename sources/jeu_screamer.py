import pygame
import time
from random import *
import fonctions
# Initialisation de pygame
pygame.init()

pygame.mixer.init()

info = pygame.display.Info()
width = int(info.current_w * 1)
height = int(info.current_h * 0.95)

font = pygame.font.Font(None, 50)
text_color = (0, 0, 0)

fenetre = pygame.display.set_mode((width,height))


scream = pygame.image.load("../data/scream.jpg")
scream = pygame.transform.scale(scream, (width,height))
screamer = pygame.image.load("../data/screamer.png")
screamer = pygame.transform.scale(screamer, (width,height))
pot = pygame.image.load("../data/pot.png")
pot = pygame.transform.scale(pot, (100,100))
#noir = pygame.image.load("../data/noir.jpg")
#noir = pygame.transform.scale(noir, (100,50))
heart = pygame.image.load("../data/heart.png")
heart = pygame.transform.scale(heart, (100,100))
bouche = pygame.image.load("../data/pot.png")
bouche = pygame.transform.scale(bouche, (100,100))

def jeu_scream():





    clock = pygame.time.Clock()

    #screamer settings
    x_screamer = 0
    mvmt = 10
    x_bouche = width//2-(width*5//100)
    finX_bouche = x_bouche + 100
    y_bouche = height//2+(height//10)
    finY_bouche = height//2

    #object settings
    x_pot = width//2
    milieu_pot = x_pot + 50


    y_pot = height+20
    vitesse_pot = -5

    score = 0
    life = ["heart1", "heart2", "heart3"]
    show_life = True
    x_heart = width//10
    y_heart = height // 10
    fin = False




    while not fin:

        milieuX_pot = x_pot + 50

        text = font.render(str(score), True, text_color)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin = True
                fonctions.leaving()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            x_screamer += mvmt
            x_bouche += mvmt
            finX_bouche = x_bouche + 100

        if keys[pygame.K_LEFT]:
            x_screamer -= mvmt
            x_bouche -= mvmt
            finX_bouche = x_bouche + 100



        if y_pot <= 0:
            x_pot = randint(width//5, width*4//5)
            milieu_pot = x_pot + 50
            y_pot = height + 20
            life.pop()

        elif milieu_pot > x_bouche and milieu_pot < finX_bouche and y_pot < y_bouche and y_pot > finY_bouche:
            score += 1
            y_pot = height + 20
            x_pot = randint(width//5, width*4//5)
            milieu_pot = x_pot + 50
            mvmt += 0.2
            vitesse_pot += -0.2

        if len(life) == 0:
            fin = True



        y_pot += vitesse_pot

        """
            print(width, height)
            print(x_bouche)
            print(finX_bouche)
            print(y_bouche)
            print(finY_bouche)
            print(milieuX_pot)
        """

        fenetre.blit(scream, (0, 0))
        fenetre.blit(screamer, (x_screamer, 0))
        fenetre.blit(pot, (x_pot, y_pot))
        fenetre.blit(text,(width /2, height//5))

        x_heart = width//10
        for i in range(len(life)):
            fenetre.blit(heart,(x_heart, y_heart))
            x_heart += 100
        #fenetre.blit(noir, (x_bouche, y_bouche))


        clock.tick(200)
        pygame.display.flip()












