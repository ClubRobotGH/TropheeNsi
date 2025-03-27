from math import *
import pygame
import time
import fonctions
pygame.init()
info = pygame.display.Info()
#trouve la taille de l'écran pour ouvrir pygame en plein écran
width = int(info.current_w *1)
height = int(info.current_h * 1)
fenetre = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
#importe les images

#fond Musée
fondécran = pygame.image.load("../data/FondMusée.png")
fondécran = pygame.transform.scale(fondécran,(width,height))
vitesse = width//400 #la vitesse de déplacement des objets



def calculeDuScore(positions, bonnePositions, coefficientAgrandissement, oeuvre):
    """
    Calcule et affiche le score basé sur la distance entre les positions actuelles et les bonnes positions
    tout en prenant en compte les erreurs du joueur.

    paramètres:
        positions: liste des positions actuelles des objets
        bonnePositions: liste des bonnes positions
        coefficientAgrandissement: facteur d'échelle pour l'ajustement des positions
        oeuvre: l'objet représenté dans le jeu (tableau)
    """


    somme = 0

    # Calculer la précision de la positions de chaque orrifice
    for i in range(len(positions)):    
        print(positions[i])
        print(type(positions[i][0]),type(positions[i][1]),type(bonnePositions[i][0]),type(bonnePositions[i][1]))
        somme += abs((positions[i][0]/coefficientAgrandissement-bonnePositions[i][0])/bonnePositions[i][0])
        somme += abs((positions[i][1]/coefficientAgrandissement-bonnePositions[i][1])/bonnePositions[i][0])

    moy = somme / (2*len(positions)) * 100
    score = max(100-moy,0)#s'assure que le score soit au moins de 0
    score = round(score)
    # Afficher le score comme un pourcentage
    for s in range(-1, score):
        fenetre.blit(fondécran, (0, 0))
        fenetre.blit(oeuvre[0], (tableau.coinHG[0], tableau.coinHG[1]))

        # Afficher les orifices à leurs positions actuelles
        for orifices in positions:
            fenetre.blit(orifices[2], (orifices[0], orifices[1]))

        # Affichage du score avec un pourcentage d'avancement
        fonctions.afficher_texte(str(s+1)+" %", width // 2 - 10 * coefficientAgrandissement,
                                 height // 2 - 5 * coefficientAgrandissement, (255, 255, 255),
                                 "../data/polices/04b_30/04B_30__.TTF")

        # Mettre à jour l'écran et faire une pause
        pygame.display.flip()
        time.sleep(0.01)

# on charge toute les images de Marilyn Monroe
class marilynMonroe:
    fondTableau = pygame.image.load("../data/MarilynMonroeVide.jpg")
    coefficientAgrandissement = min(width//fondTableau.get_size()[0],height//fondTableau.get_size()[1]) #cette variable permet de savoir par combien on doit multiplier la taille de chacune des images (et coordonées) pour le plein écran.
    fondTableau = pygame.transform.scale(fondTableau,(fondTableau.get_size()[0]*coefficientAgrandissement,fondTableau.get_size()[1]*coefficientAgrandissement))

    OeuilDroit = pygame.image.load("../data/MmOD.png")
    OeuilDroit = pygame.transform.scale(OeuilDroit,(OeuilDroit.get_size()[0]*coefficientAgrandissement,OeuilDroit.get_size()[1]*coefficientAgrandissement))
    OeuilGauche = pygame.image.load("../data/MmOG.png")
    OeuilGauche = pygame.transform.scale(OeuilGauche,(OeuilGauche.get_size()[0]*coefficientAgrandissement,OeuilGauche.get_size()[1]*coefficientAgrandissement))
    Bouche = pygame.image.load("../data/MmB.png")
    Bouche = pygame.transform.scale(Bouche,(Bouche.get_size()[0]*coefficientAgrandissement,Bouche.get_size()[1]*coefficientAgrandissement))
    Nez = pygame.image.load("../data/MmN.png")
    Nez = pygame.transform.scale(Nez,(Nez.get_size()[0]*coefficientAgrandissement,Nez.get_size()[1]*coefficientAgrandissement))
    #calcule les coins en haut a gauche et a droite pour centrer le tableau
    coinHG = [(width-fondTableau.get_size()[0])//2,(height-fondTableau.get_size()[1])//2]
    largeurImage,hauteurImage = fondTableau.get_size()
    coinBD = [coinHG[0]+largeurImage,coinHG[1]+hauteurImage]
    Orifices = [fondTableau,OeuilGauche,OeuilDroit,Bouche,Nez]
    bonnePositions = [(179,120),(233,118),(400,173),(207,139)] #les positions originales de chacun orifices à l'origine.
    #cette listes contient la possition de chacun des oririfices
    positions = [[coinHG[0],coinHG[1],Orifices[1]]]

class monaLisa:
    # on charge toute les images de la mona lisa
    fondMonaLisa = pygame.image.load("../data/monaLisaVide.jpg")
    coefficientAgrandissement = min(width//fondMonaLisa.get_size()[0],height//fondMonaLisa.get_size()[1]) #cette variable permet de savoir par combien on doit multiplier la taille de chacune des images (et coordonées) pour le plein écran.
    fondMonaLisa = pygame.transform.scale(fondMonaLisa,(fondMonaLisa.get_size()[0]*coefficientAgrandissement,fondMonaLisa.get_size()[1]*coefficientAgrandissement))

    MLOD = pygame.image.load("../data/MLOD.png")
    MLOD = pygame.transform.scale(MLOD,(MLOD.get_size()[0]*coefficientAgrandissement,MLOD.get_size()[1]*coefficientAgrandissement))
    MLOG = pygame.image.load("../data/MLOG.png")
    MLOG = pygame.transform.scale(MLOG,(MLOG.get_size()[0]*coefficientAgrandissement,MLOG.get_size()[1]*coefficientAgrandissement))
    MLB = pygame.image.load("../data/MLB.png")
    MLB = pygame.transform.scale(MLB,(MLB.get_size()[0]*coefficientAgrandissement,MLB.get_size()[1]*coefficientAgrandissement))
    MLN = pygame.image.load("../data/MLN.png")
    MLN = pygame.transform.scale(MLN,(MLN.get_size()[0]*coefficientAgrandissement,MLN.get_size()[1]*coefficientAgrandissement))
    #calcule les coins en haut a gauche et a droite pour centrer le tableau
    coinHG = [(width-fondMonaLisa.get_size()[0])//2,(height-fondMonaLisa.get_size()[1])//2]
    largeurImage,hauteurImage = fondMonaLisa.get_size()
    coinBD = [coinHG[0]+largeurImage,coinHG[1]+hauteurImage]
    Orifices = [fondMonaLisa,MLOG,MLOD,MLB,MLN]
    bonnePositions = [(397,191),(459,190),(421,276),(422,186)] #les positions originales de chacun orifices à l'origine.
    #cette listes contient la possition de chacun des oririfices
    positions = [[coinHG[0],coinHG[1],Orifices[1]]]

class jeuneFilleALaPerle:
    # on charge toute les images de la jeune fille a la perle
    fondJeuneFilleALaPerle = pygame.image.load("../data/jeuneFilleALaPerleVide.jpg")
    coefficientAgrandissement = min(width//fondJeuneFilleALaPerle.get_size()[0],height//fondJeuneFilleALaPerle.get_size()[1]) #cette variable permet de savoir par combien on doit multiplier la taille de chacune des images (et coordonées) pour le plein écran.
    fondJeuneFilleALaPerle = pygame.transform.scale(fondJeuneFilleALaPerle,(fondJeuneFilleALaPerle.get_size()[0]*coefficientAgrandissement,fondJeuneFilleALaPerle.get_size()[1]*coefficientAgrandissement))
    JfalpOD = pygame.image.load("../data/JfalpOD.png")
    JfalpOD = pygame.transform.scale(JfalpOD,(JfalpOD.get_size()[0]*coefficientAgrandissement,JfalpOD.get_size()[1]*coefficientAgrandissement))
    JfalpOG = pygame.image.load("../data/JfalpOG.png")
    JfalpOG = pygame.transform.scale(JfalpOG,(JfalpOG.get_size()[0]*coefficientAgrandissement,JfalpOG.get_size()[1]*coefficientAgrandissement))
    JfalpB = pygame.image.load("../data/JfalpB.png")
    JfalpB = pygame.transform.scale(JfalpB,(JfalpB.get_size()[0]*coefficientAgrandissement,JfalpB.get_size()[1]*coefficientAgrandissement))
    JfalpN = pygame.image.load("../data/JfalpN.png")
    JfalpN = pygame.transform.scale(JfalpN,(JfalpN.get_size()[0]*coefficientAgrandissement,JfalpN.get_size()[1]*coefficientAgrandissement))
    #calcule les coins en haut a gauche et a droite pour centrer le tableau
    coinHG = [(width-fondJeuneFilleALaPerle.get_size()[0])//2,(height-fondJeuneFilleALaPerle.get_size()[1])//2]
    largeurImage,hauteurImage = fondJeuneFilleALaPerle.get_size()
    coinBD = [coinHG[0]+largeurImage,coinHG[1]+hauteurImage]
    Orifices = [fondJeuneFilleALaPerle,JfalpOG,JfalpOD,JfalpB,JfalpN]
    bonnePositions = [(125,105),(152,107),(132,151),(150,88)] #les positions originales de chacun orifices à l'origine.
    #cette listes contient la possition de chacun des oririfices
    positions = [[coinHG[0],coinHG[1],Orifices[1]]]



def refaireTableau(oeuvre:str):
    """
    fonction qui gère le jeu ou on doit reconstituer les tableau

    paramètres:
        oeuvre(str): le tableau qu'on veut refaire
    """
    global tableau
    if oeuvre == "monaLisa":
        tableau = monaLisa
    elif oeuvre == "jeuneFilleALaPerle":
        tableau = jeuneFilleALaPerle
    else:
        tableau = marilynMonroe
    selected = 0 #le 0eme orifices (oueil gauche)
    running = True
    fini = False #si le joueur a placé tout les oriffices
    while running:
        for event in pygame.event.get():
            #si l'utilisateur clique sur la croix, on quitte le jeu
            if event.type == pygame.QUIT:
                running = False
                fonctions.leaving()
        # Detect key press
        keys = pygame.key.get_pressed()
        #pour chaque directions, on s'assure de ne pas sortir du tableau
        if keys[pygame.K_UP]:
            if tableau.positions[selected][1] > tableau.coinHG[1]:
                tableau.positions[selected][1] -= vitesse  #en haut
        if keys[pygame.K_DOWN]:#en bas
            if tableau.positions[selected][1]+tableau.Orifices[selected+1].get_size()[1] < tableau.coinBD[1]:
                tableau.positions[selected][1] += vitesse
        if keys[pygame.K_LEFT]:
            if tableau.positions[selected][0] > tableau.coinHG[0]:
                tableau.positions[selected][0] -= vitesse  #gauche
        if keys[pygame.K_RIGHT]:
            if tableau.positions[selected][0]+tableau.Orifices[selected+1].get_size()[0] < tableau.coinBD[0]:
                tableau.positions[selected][0] += vitesse  #droite
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:#passe au prochain orrifice
            if selected < len(tableau.Orifices)-2:
                selected+=1
                tableau.positions.append([tableau.coinHG[0],tableau.coinHG[1],tableau.Orifices[selected+1]])
            else:
                running = False
                fini = True
        if keys[pygame.K_BACKSPACE]: #passe a l'orifice précédent
            if selected > 0:
                selected-=1
        fenetre.blit(fondécran,(0,0))
        fenetre.blit(tableau.Orifices[0],(tableau.coinHG[0],tableau.coinHG[1]))
        for orifices in tableau.positions:
            fenetre.blit(orifices[2],(orifices[0],orifices[1]))
        clock.tick(60)
        pygame.display.flip()
        while keys[pygame.K_RETURN] or keys[pygame.K_BACKSPACE] or keys[pygame.K_SPACE]: #évite de passer plusieurs orifices d'un coup si l'utilisateur reste plus d'un tick
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
    print(tableau.positions)
    print(tableau.coefficientAgrandissement)

    if fini:
        calculeDuScore(tableau.positions, tableau.bonnePositions, tableau.coefficientAgrandissement, tableau.Orifices)
    tableau.positions = [[tableau.coinHG[0],tableau.coinHG[1],tableau.Orifices[1]]]#on remet le jeu a 0 pour pouvoir y rejouer
    time.sleep(5)
