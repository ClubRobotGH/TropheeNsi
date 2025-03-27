import pygame
import time
from random import *
import os
os.chdir(os.path.abspath(__file__)[:-7]) #pour régler le probleme de chemin d'acces qu'on a eu avec certains IDE
import jeu_screamer
import fonctions
import refaireTableau
import jeu_dinosaure
import VraiOuFaux
# Initialisation de pygame
pygame.init()

pygame.mixer.init()

info = pygame.display.Info()
width = int(info.current_w * 1)
height = int(info.current_h * 1)

fenetre = pygame.display.set_mode((width,height))
RED = (255, 0, 0)

pygame.display.set_caption("Artisery Quest")
pygame.display.set_icon(pygame.image.load("../data/logo.png"))
minimum = height
if height > width:
    minimum = width

sprite = pygame.image.load("../data/sprite.png")
sprite = pygame.transform.scale(sprite, (100,100))
rideau = pygame.image.load("../data/rideau.png")
rideau = pygame.transform.scale(rideau, (width,height))
fleche = pygame.image.load("../data/fleche.jpg")
fleche = pygame.transform.scale(fleche, (width//5,height//8))
bateau = pygame.image.load("../data/bateau.png")
bateau = pygame.transform.scale(bateau, (100,100))
fond = pygame.image.load("../data/fond_musee.jpg")
fond = pygame.transform.scale(fond, (width,height))
monalisa = pygame.image.load("../data/monalisa.jpg")
monalisa = pygame.transform.scale(monalisa, (minimum,height))
monroe = pygame.image.load("../data/monroe.jpg")
monroe = pygame.transform.scale(monroe, (minimum,height))
perle = pygame.image.load("../data/perle.jpg")
perle = pygame.transform.scale(perle, (minimum,height))
monalisa = pygame.image.load("../data/monalisa.jpg")
monalisa = pygame.transform.scale(monalisa, (minimum,height))
scream = pygame.image.load("../data/peinture_scream.jpg")
scream = pygame.transform.scale(scream, (minimum,height))
vague = pygame.image.load("../data/vague_fond.jpg")
vague = pygame.transform.scale(vague,(minimum,height))
enchere = pygame.image.load("../data/enchere.jpeg")
enchere = pygame.transform.scale(enchere,(minimum,height))
peinture = "monalisa"
image = monalisa


def changer_image():
    """
    Cette fonction permet de changer d'image lorsqu'on appuie sur le bouton.

    """
    global image, peinture

    if peinture == "monalisa":
        fenetre.blit(fond, (0, 0))
        image = monroe
        peinture = "monroe"


    elif peinture == "monroe":
        fenetre.blit(fond, (0, 0))
        image = perle
        peinture = "perle"

    elif peinture == "perle":
        fenetre.blit(fond, (0, 0))
        image = scream
        peinture = "scream"

    elif peinture == "scream":
        fenetre.blit(fond, (0, 0))
        image = vague
        peinture = "vague"

    elif peinture == "vague":
        fenetre.blit(fond,(0,0))
        image = enchere
        peinture = "enchere"

    elif peinture == "enchere":
        fenetre.blit(fond,(0,0))
        image = monalisa
        peinture = "monalisa"



def jeu():

    global image, peinture

    click = False

    fin = False


    while not fin:



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin = True



        fonctions.bouton(fleche,width*4//5,height//2,100,100)

        if fonctions.bouton(fleche,width*4//5,height//2,100,100):
            click = True
            changer_image()
            pygame.time.wait(150)
            click = False


        fenetre.blit(fond, (0, 0))
        fonctions.bouton(image,(width-minimum)//2,0,minimum,height)
        fonctions.bouton(fleche,width*4//5,height//2,100,100)


        #print(fontions.bouton(image,(width-minimum)//2,0,minimum,height))
        if fonctions.bouton(image,(width-minimum)//2,0,minimum,height):
            if peinture == "scream":
                jeu_screamer.jeu_scream()
            if peinture == "perle":
                refaireTableau.refaireTableau("jeuneFilleALaPerle")
            elif peinture == "monalisa":
                refaireTableau.refaireTableau("monaLisa")
            elif peinture == "monroe":
                refaireTableau.refaireTableau("monroe")
            elif peinture == "vague":
                jeu_dinosaure.jeu()
            elif peinture == "enchere":
                VraiOuFaux.VraiOuFaux()


        pygame.display.flip()




jeu()
pygame.time.wait(1000)
pygame.quit()











