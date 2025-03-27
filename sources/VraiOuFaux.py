from math import *
import pygame
import time
import random
import fonctions
#import fonctions

pygame.init()
info = pygame.display.Info()
#trouve la taille de l'écran pour ouvrir pygame en plein écran
width = int(info.current_w *1)
height = int(info.current_h * 1)
fenetre = pygame.display.set_mode((width, height))




#on prépare  une carte tableau vide
coinHG = (width//3,height//6)
dimensionCarte = (width//3,2*height//3)
carteVide = pygame.Surface(dimensionCarte)
carteVide.fill((255,255,255))


#importe les images

#fond Musée
fondécran = pygame.image.load("../data/enchere.jpeg")
fondécran = pygame.transform.scale(fondécran,(width,height))
#boutons
croix = pygame.image.load("../data/croix.png")
croix = pygame.transform.scale(croix,(width//10,width//10))
check = pygame.image.load("../data/check.png")
check = pygame.transform.scale(check,(width//10,width//10))
#tableaux
marilynMonroe = pygame.image.load("../data/MarilynMonroe.jpg")
marilynMonroe = pygame.transform.scale(marilynMonroe,(round(marilynMonroe.get_size()[0]*min(dimensionCarte[0]/marilynMonroe.get_size()[0],dimensionCarte[1]/3/marilynMonroe.get_size()[1])),round(marilynMonroe.get_size()[1]*min(dimensionCarte[0]/marilynMonroe.get_size()[0],dimensionCarte[1]/3/marilynMonroe.get_size()[1]))))
americanGothic = pygame.image.load("../data/americanGothic.jpg")
americanGothic = pygame.transform.scale(americanGothic,(round(americanGothic.get_size()[0]*min(dimensionCarte[0]/americanGothic.get_size()[0],dimensionCarte[1]/3/americanGothic.get_size()[1])),round(americanGothic.get_size()[1]*min(dimensionCarte[0]/americanGothic.get_size()[0],dimensionCarte[1]/3/americanGothic.get_size()[1]))))
guernica = pygame.image.load("../data/guernica.jpeg")
guernica = pygame.transform.scale(guernica,(round(guernica.get_size()[0]*min(dimensionCarte[0]/guernica.get_size()[0],dimensionCarte[1]/3/guernica.get_size()[1])),round(guernica.get_size()[1]*min(dimensionCarte[0]/guernica.get_size()[0],dimensionCarte[1]/3/guernica.get_size()[1]))))
laPersistanceDeLaMemoire = pygame.image.load("../data/la persistance de la mémoire.jpg")
laPersistanceDeLaMemoire = pygame.transform.scale(laPersistanceDeLaMemoire,(round(laPersistanceDeLaMemoire.get_size()[0]*min(dimensionCarte[0]/laPersistanceDeLaMemoire.get_size()[0],dimensionCarte[1]/3/laPersistanceDeLaMemoire.get_size()[1])),round(laPersistanceDeLaMemoire.get_size()[1]*min(dimensionCarte[0]/laPersistanceDeLaMemoire.get_size()[0],dimensionCarte[1]/3/laPersistanceDeLaMemoire.get_size()[1]))))
leCri = pygame.image.load("../data/le cri.jpeg")
leCri = pygame.transform.scale(leCri,(round(leCri.get_size()[0]*min(dimensionCarte[0]/leCri.get_size()[0],dimensionCarte[1]/3/leCri.get_size()[1])),round(leCri.get_size()[1]*min(dimensionCarte[0]/leCri.get_size()[0],dimensionCarte[1]/3/leCri.get_size()[1]))))
ménines = pygame.image.load("../data/ménines.jpeg")
ménines = pygame.transform.scale(ménines,(round(ménines.get_size()[0]*min(dimensionCarte[0]/ménines.get_size()[0],dimensionCarte[1]/3/ménines.get_size()[1])),round(ménines.get_size()[1]*min(dimensionCarte[0]/ménines.get_size()[0],dimensionCarte[1]/3/ménines.get_size()[1]))))
monaLisa = pygame.image.load("../data/monaLisa.jpg")
monaLisa = pygame.transform.scale(monaLisa,(round(monaLisa.get_size()[0]*min(dimensionCarte[0]/monaLisa.get_size()[0],dimensionCarte[1]/3/monaLisa.get_size()[1])),round(monaLisa.get_size()[1]*min(dimensionCarte[0]/monaLisa.get_size()[0],dimensionCarte[1]/3/monaLisa.get_size()[1]))))
nuitEtoilee = pygame.image.load("../data/nuitEtoilée.jpg")
nuitEtoilee = pygame.transform.scale(nuitEtoilee,(round(nuitEtoilee.get_size()[0]*min(dimensionCarte[0]/nuitEtoilee.get_size()[0],dimensionCarte[1]/3/nuitEtoilee.get_size()[1])),round(nuitEtoilee.get_size()[1]*min(dimensionCarte[0]/nuitEtoilee.get_size()[0],dimensionCarte[1]/3/nuitEtoilee.get_size()[1]))))
ophelia = pygame.image.load("../data/ophelia.jpg")
ophelia = pygame.transform.scale(ophelia,(round(ophelia.get_size()[0]*min(dimensionCarte[0]/ophelia.get_size()[0],dimensionCarte[1]/3/ophelia.get_size()[1])),round(ophelia.get_size()[1]*min(dimensionCarte[0]/ophelia.get_size()[0],dimensionCarte[1]/3/ophelia.get_size()[1]))))
tournesols = pygame.image.load("../data/tournesols.jpg")
tournesols = pygame.transform.scale(tournesols,(round(tournesols.get_size()[0]*min(dimensionCarte[0]/tournesols.get_size()[0],dimensionCarte[1]/3/tournesols.get_size()[1])),round(tournesols.get_size()[1]*min(dimensionCarte[0]/tournesols.get_size()[0],dimensionCarte[1]/3/tournesols.get_size()[1]))))
VIII = pygame.image.load("../data/VIII.jpeg")
VIII = pygame.transform.scale(VIII,(round(VIII.get_size()[0]*min(dimensionCarte[0]/VIII.get_size()[0],dimensionCarte[1]/3/VIII.get_size()[1])),round(VIII.get_size()[1]*min(dimensionCarte[0]/VIII.get_size()[0],dimensionCarte[1]/3/VIII.get_size()[1]))))
leDejeuner = pygame.image.load("../data/leDéjeunerSurLherbe.jpeg")
leDejeuner = pygame.transform.scale(leDejeuner,(round(leDejeuner.get_size()[0]*min(dimensionCarte[0]/leDejeuner.get_size()[0],dimensionCarte[1]/3/leDejeuner.get_size()[1])),round(leDejeuner.get_size()[1]*min(dimensionCarte[0]/leDejeuner.get_size()[0],dimensionCarte[1]/3/leDejeuner.get_size()[1]))))
jeuneFilleALaPerle = pygame.image.load("../data/jeuneFilleALaPerle.jpg")
jeuneFilleALaPerle = pygame.transform.scale(jeuneFilleALaPerle,(round(jeuneFilleALaPerle.get_size()[0]*min(dimensionCarte[0]/jeuneFilleALaPerle.get_size()[0],dimensionCarte[1]/3/jeuneFilleALaPerle.get_size()[1])),round(jeuneFilleALaPerle.get_size()[1]*min(dimensionCarte[0]/jeuneFilleALaPerle.get_size()[0],dimensionCarte[1]/3/jeuneFilleALaPerle.get_size()[1]))))
jardinDesDelices = pygame.image.load("../data/jardin des délices.jpg")
jardinDesDelices =  pygame.transform.scale(jardinDesDelices,(round(jardinDesDelices.get_size()[0]*min(dimensionCarte[0]/jardinDesDelices.get_size()[0],dimensionCarte[1]/3/jardinDesDelices.get_size()[1])),round(jardinDesDelices.get_size()[1]*min(dimensionCarte[0]/jardinDesDelices.get_size()[0],dimensionCarte[1]/3/jardinDesDelices.get_size()[1]))))

ordreTableau = [marilynMonroe,monaLisa,tournesols,guernica,laPersistanceDeLaMemoire,leCri,ménines,jeuneFilleALaPerle,nuitEtoilee,jardinDesDelices,leDejeuner,ophelia,VIII,americanGothic]
print(width,height)
tailleDePolice = height//40
infosTableau = [
    # Niveau 1 (facile) :
    {"Nom": ("Marilyn Diptych", "Lots Of Marilyn"), "Auteur": ("Andy Warhol", "Vincent van Gogh"), "Date": ("1962", "1862"), "Type": ("Acrylique", "Huile"), "Technique": ("Sérigraphie", "Fusain"), "Mouvement": ("Pop art", "Réalisme"), "Localisation": ("Tate Modern", "MET")},

    {"Nom": ("La Joconde", "Le Sourire Perdu"), "Auteur": ("Léonard de Vinci", "Michel-Ange"), "Date": ("1503", "1703"), "Type": ("Huile sur bois", "Aquarelle"), "Technique": ("Sfumato", "Pointillisme"), "Mouvement": ("Renaissance", "Baroque"), "Localisation": ("Louvre", "Musée d'Orsay")},

    {"Nom": ("Les Tournesols", "Fleurs d'été"), "Auteur": ("Vincent van Gogh", "Claude Monet"), "Date": ("1888", "1788"), "Type": ("Huile sur toile", "Pastel"), "Technique": ("Empâtement", "Fresque"), "Mouvement": ("Post-impressionnisme", "Expressionnisme"), "Localisation": ("National Gallery", "Musée du Prado")},

    # Niveau 2 (moyen) :
    {"Nom": ("Guernica", "La Guerre Civile"), "Auteur": ("Pablo Picasso", "Salvador Dalí"), "Date": ("1937", "1927"), "Type": ("Huile sur toile", "Acrylique"), "Technique": ("Cubisme", "Surréalisme"), "Mouvement": ("Cubisme", "Dadaïsme"), "Localisation": ("Museo Reina Sofía", "Centre Pompidou")},

    {"Nom": ("La Persistance de la mémoire", "Les Horloges fondues"), "Auteur": ("Salvador Dalí", "René Magritte"), "Date": ("1931", "1941"), "Type": ("Huile sur toile", "Gouache"), "Technique": ("Surréalisme", "Impressionnisme"), "Mouvement": ("Surréalisme", "Symbolisme"), "Localisation": ("MoMA", "Musée du Louvre")},

    {"Nom": ("Le Cri", "L'Angoisse"), "Auteur": ("Edvard Munch", "Francis Bacon"), "Date": ("1893", "1903"), "Type": ("Huile, tempera et pastel", "Aquarelle"), "Technique": ("Expressionnisme", "Cubisme"), "Mouvement": ("Expressionnisme", "Futurisme"), "Localisation": ("Galerie nationale d'Oslo", "Tate Modern")},

    # Niveau 3 (difficile) :
    {"Nom": ("Les Ménines", "Les Dames de Cour"), "Auteur": ("Diego Velázquez", "Francisco Goya"), "Date": ("1656", "1676"), "Type": ("Huile sur toile", "Encre de Chine"), "Technique": ("Baroque", "Rococo"), "Mouvement": ("Baroque", "Néo-classicisme"), "Localisation": ("Musée du Prado", "Galerie des Offices")},

    {"Nom": ("La Jeune Fille à la perle", "La Femme au collier"), "Auteur": ("Johannes Vermeer", "Rembrandt"), "Date": ("1665", "1625"), "Type": ("Huile sur toile", "Fresque"), "Technique": ("Clair-obscur", "Pointillisme"), "Mouvement": ("Baroque", "Romantisme"), "Localisation": ("Mauritshuis", "Rijksmuseum")},

    {"Nom": ("La Nuit étoilée", "Le Ciel en tourmente"), "Auteur": ("Vincent van Gogh", "Paul Gauguin"), "Date": ("1889", "1879"), "Type": ("Huile sur toile", "Fusain"), "Technique": ("Post-impressionnisme", "Surréalisme"), "Mouvement": ("Post-impressionnisme", "Expressionnisme"), "Localisation": ("MoMA", "Musée d'Orsay")},

    # Niveau 4 (très difficile) :
    {"Nom": ("Le Jardin des délices", "L'Enfer et le Paradis"), "Auteur": ("Hieronymus Bosch", "Albrecht Dürer"), "Date": ("1503-1515", "1483-1495"), "Type": ("Huile sur panneau de bois", "Enluminure"), "Technique": ("Triptyque", "Fresque"), "Mouvement": ("Renaissance nordique", "Gothique"), "Localisation": ("Musée du Prado", "Louvre")},

    {"Nom": ("Le Déjeuner sur l'herbe", "Les Amis champêtres"), "Auteur": ("Édouard Manet", "Claude Monet"), "Date": ("1863", "1883"), "Type": ("Huile sur toile", "Pastel"), "Technique": ("Impressionnisme", "Réalisme"), "Mouvement": ("Impressionnisme", "Rococo"), "Localisation": ("Musée d'Orsay", "National Gallery")},

    {"Nom": ("Ophelia", "La Nymphe noyée"), "Auteur": ("John Everett Millais", "Dante Gabriel Rossetti"), "Date": ("1851-1852", "1861-1862"), "Type": ("Huile sur toile", "Aquarelle"), "Technique": ("Préraphaélite", "Symbolisme"), "Mouvement": ("Préraphaélisme", "Romantisme"), "Localisation": ("Tate Britain", "Musée du Prado")},

    {"Nom": ("Composition VIII", "Abstraction Dynamique"), "Auteur": ("Wassily Kandinsky", "Piet Mondrian"), "Date": ("1923", "1913"), "Type": ("Huile sur toile", "Gouache"), "Technique": ("Abstraction géométrique", "Surréalisme"), "Mouvement": ("Abstraction", "Expressionnisme"), "Localisation": ("Guggenheim Museum", "Centre Pompidou")},

    {"Nom": ("American Gothic", "Midwest Farmers"), "Auteur": ("Grant Wood", "Edward Hopper"), "Date": ("1930", "1920"), "Type": ("Huile sur bois", "Acrylique"), "Technique": ("Réalisme américain", "Cubisme"), "Mouvement": ("Régionalisme", "Surréalisme"), "Localisation": ("Art Institute of Chicago", "MoMA")}
]


def VraiOuFaux():
    running = True
    faux = [random.randint(0, len(ordreTableau)-1) for _ in range(1)] #génère une list d'indices des tableau dont certaines informations seront fausse
    cartes = ["e"]*(len(ordreTableau))
    for indiceTableau in range(len(ordreTableau)):#on génère toutes les carte du jeu avec certaines infos justes et d'autre fausses
        cartes[indiceTableau] = carteVide.copy()
        cartes[indiceTableau].blit(ordreTableau[indiceTableau],((dimensionCarte[0]-ordreTableau[indiceTableau].get_size()[0])//2,(dimensionCarte[1]//3-ordreTableau[indiceTableau].get_size()[1])//2)) #on ajoute le tableau au milieu du haut de la carte
        texte = "\n"
        if indiceTableau in faux:
            #si jamais la carte est censé etre fausse, on prévoit entre 1 et 5 fausses informations
            fauxObligé = random.choices(list(infosTableau[indiceTableau].items()),k=random.randint(1,len(infosTableau[indiceTableau].items())-1))
            for infos in infosTableau[indiceTableau].items():
                if infos in fauxObligé:
                    texte += infos[0]+" : "+infos[1][1]+"\n"*2
                else:
                    texte += infos[0]+" : "+infos[1][1]+"\n"*2
        else:
            for infos in infosTableau[indiceTableau].items():
                texte += infos[0]+" : "+infos[1][0]+"\n"*2
        fonctions.afficher_texte(texte,0,dimensionCarte[1]//3,(0,0,0),"../data/polices/geoform/geoform.otf",tailleDePolice,cartes[indiceTableau])


    nombreErreurs = 0
    indiceErreurs = []
    for indiceTableau in range(len(ordreTableau)):
        fenetre.blit(fondécran,(0,0))
        fenetre.blit(cartes[indiceTableau],(coinHG))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                #si l'utilisateur clique sur la croix, on quitte le jeu
                if event.type == pygame.QUIT:
                    waiting = False
                    fonctions.leaving()
            fenetre.blit(fondécran,(0,0))
            fenetre.blit(cartes[indiceTableau],coinHG)
            if indiceTableau == 0:
                fonctions.afficher_texte("Certains de ces tableaux sont faux, a vous retrouver les bons tableau, graces a leurs informations",width//10,height//10,(255,255,255),"../data/polices/geoform/geoform-Bold.otf",floor(tailleDePolice*1.25))
            if fonctions.bouton(check,width//10,height-width//5,width//10,width//10):
                waiting = False
                if indiceTableau in faux:
                    nombreErreurs += 1
                    indiceErreurs.append(indiceTableau)
            if fonctions.bouton(croix,width-width//5,height-width//5,width//10,width//10):
                waiting = False
                if not indiceTableau in faux:
                    nombreErreurs += 1
                    indiceErreurs.append(indiceTableau)
            pygame.display.flip()
        while fonctions.bouton(croix,width-width//5,height-width//5,width//10,width//10) or fonctions.bouton(check,width//10,height-width//5,width//10,width//10):
            pygame.display.flip()
            for event in pygame.event.get():
                #si l'utilisateur clique sur la croix, on quitte le jeu
                if event.type == pygame.QUIT:
                    waiting = False
                    fonctions.leaving()
    if nombreErreurs == 0:
        waiting = True
        while waiting:
            for event in pygame.event.get():
                #si l'utilisateur clique sur la croix, on quitte le jeu
                if event.type == pygame.QUIT:
                    waiting = False
                    fonctions.leaving()
            fenetre.blit(fondécran,(0,0))
            fonctions.afficher_texte("Bravo, vous avez tout trouvé",width//3,height//2,(0,0,255),"../data/polices/geoform/Geoform-Bold.otf",tailleDePolice*2)
            if fonctions.bouton_texte("changer de jeu",width//3,height//6*5,50,50,(0,0,0),(0,0,0),(255,255,255)):
                waiting = False
            pygame.display.flip()
        while fonctions.bouton_texte("changer de jeu",width//3,height//6*5,50,50,(0,0,0),(0,0,0),(255,255,255)):
            pygame.display.flip()
            for event in pygame.event.get():
                #si l'utilisateur clique sur la croix, on quitte le jeu
                if event.type == pygame.QUIT:
                    fonctions.leaving()
    else:
        for erreurs in indiceErreurs:
            carteCorrigé = carteVide.copy()
            carteCorrigé.blit(ordreTableau[erreurs],((dimensionCarte[0]-ordreTableau[erreurs].get_size()[0])//2,(dimensionCarte[1]//3-ordreTableau[erreurs].get_size()[1])//2))
            texte = "\n"
            for infos in infosTableau[erreurs].items():
                texte += infos[0]+" : "+infos[1][0]+"\n"*2
            fonctions.afficher_texte(texte,0,dimensionCarte[1]//3,(0,0,0),"../data/polices/geoform/geoform.otf",tailleDePolice,carteCorrigé)
            pygame.display.flip()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    #si l'utilisateur clique sur la croix, on quitte le jeu
                    if event.type == pygame.QUIT:
                        waiting = False
                        fonctions.leaving()
                fenetre.blit(fondécran,(0,0))
                fonctions.afficher_texte("vous avez fait "+str(nombreErreurs)+" erreurs"+"\n"+"voici les bonnes réponses",width//3,height//10,(255,0,0),"../data/polices/geoform/geoform.otf",floor(tailleDePolice*1.25))
                fenetre.blit(carteCorrigé,coinHG)
                if erreurs == indiceErreurs[-1]:
                    if fonctions.bouton_texte("changer de jeu",width//3,height//6*5,50,50,(0,0,0),(0,0,0),(255,255,255)):
                        waiting = False
                else:
                    if fonctions.bouton_texte("erreur suivante",width//3,height//6*5,50,50,(0,0,0),(0,0,0),(255,255,255)):
                        waiting = False
                pygame.display.flip()
            if erreurs == indiceErreurs[-1]:
                while fonctions.bouton_texte("changer de jeu",width//3,height//6*5,50,50,(0,0,0),(0,0,0),(255,255,255)):
                    pygame.display.flip()
                    for event in pygame.event.get():
                        #si l'utilisateur clique sur la croix, on quitte le jeu
                        if event.type == pygame.QUIT:
                            waiting = False
                            fonctions.leaving()
            else:
                while fonctions.bouton_texte("erreur suivante",width//3,height//6*5,50,50,(0,0,0),(0,0,0),(255,255,255)):
                    pygame.display.flip()
                    for event in pygame.event.get():
                        #si l'utilisateur clique sur la croix, on quitte le jeu
                        if event.type == pygame.QUIT:
                            waiting = False
                            fonctions.leaving()

