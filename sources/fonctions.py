import pygame
import time

pygame.init()
info = pygame.display.Info()
#trouve la taille de l'écran pour ouvrir pygame en plein écran
width = int(info.current_w *1)
height = int(info.current_h * 1)
fenetre = pygame.display.set_mode((width, height))
sortie = pygame.image.load("../data/louvre.jpg")
sortie = pygame.transform.scale(sortie,(width,height))



def bouton(image, x:int, y:int, l:int, h:int, agrandissement=False):
    """
    Cette fonction permet d'afficher un bouton dans la fenetre a partir d'une image et retourne l'état de ce bouton.
    Peut aussi faire une hitbox si imaage vaut 0

    Cette fonction est entièrement crée par Esteban ROUVIERE

    parametres:
        image(<class 'pygame.surface.Surface'>) : l'image a afficher comme bouton, (0 pour faire un image transparent, une hitbox)

        x(int) : l'abscisse du bouton

        y(int) : l'ordonnée du bouton

        l(int) : la largeur du bouton

        h(int) : la hauteur du bouton

        agrandissement(bool) : permet de faire grossir l'image qunad la souris passe dessus (encore en test)

    sortie:
        (bool): si le bouton est cliqué ou pas
    """
    souris = pygame.mouse.get_pos()
    clic = pygame.mouse.get_pressed()
    if image != 0:
        image = pygame.transform.scale(image,(l,h))
    if x + l > souris[0] > x and y + h > souris[1] > y:
        if image != 0:
            # Image agrandie
            if agrandissement:
                image = pygame.transform.scale(image, (l * 105 // 100, h * 105 // 100))
                fenetre.blit(image, (x - (l * 105 // 100 - l) // 2, y - (h * 105 // 100 - h) // 2))
            else:
                fenetre.blit(image,(x,y))
        if clic[0]:
            return True
    # Image normale
    else:
        if image != 0:
            fenetre.blit(image, (x, y))
    return False

def bouton_texte(texte:str, x:int, y:int, largeur:int, hauteur:int, couleur1:tuple, couleur2:tuple, couleurtexte:tuple, font="../data/polices/geoform/geoform.otf"):
    """
    Cette fonction dessine un bouton interactif dans une fenêtre Pygame. Le bouton change de couleur lorsque la souris le survole,
    et exécute une action si l'utilisateur clique dessus.

    Cette fonction a été crée par notre professeur M.Maurice et modifié pour changer la police et la sortie (originalement, cela apellait une fonction, maintenant, cela renvoie un booléen)

    Paramètres :
    -----------
        texte (str) : Le texte à afficher à l'intérieur du bouton.

        x (int) : La position en pixels sur l'axe des abscisses (horizontal) où le bouton commence à être dessiné.

        y (int) : La position en pixels sur l'axe des ordonnées (vertical) où le bouton commence à être dessiné.

        largeur (int) : La largeur souhaitée du bouton. La largeur réelle sera ajustée en fonction de la taille du texte.

        hauteur (int) : La hauteur souhaitée du bouton. La hauteur réelle sera ajustée en fonction de la taille du texte.

        couleur1 (tuple) : La couleur du bouton sous forme de tuple (R, G, B) lorsque la souris n'est pas dessus.

        couleur2 (tuple) : La couleur du bouton sous forme de tuple (R, G, B) lorsque la souris survole le bouton.

        couleurtexte (tuple) : La couleur du texte du bouton sous forme de tuple (R, G, B).

    sortie:
        (bool): si le bouton est cliqué
    """
    texte = texte.upper()
    font = pygame.font.Font(font, 36)
    # Calculer la taille du texte
    largeur_texte, hauteur_texte = font.size(texte)
    largeur_bouton = max(largeur, largeur_texte + 20)  # Ajouter un peu de marge
    hauteur_bouton = max(hauteur, hauteur_texte + 10)  # Ajouter un peu de marge

    souris = pygame.mouse.get_pos()
    clic = pygame.mouse.get_pressed()

    # Détection de survol de la souris
    if x + largeur_bouton > souris[0] > x and y + hauteur_bouton > souris[1] > y:
        pygame.draw.rect(fenetre, couleur2, (x, y, largeur_bouton, hauteur_bouton))
        if clic[0] == 1:
            time.sleep(0.2)
            return True
    else:
        pygame.draw.rect(fenetre, couleur1, (x, y, largeur_bouton, hauteur_bouton))

    # Dessiner le texte centré dans le bouton
    texte_surface = font.render(texte, True, couleurtexte)
    texte_rect = texte_surface.get_rect(center=(x + largeur_bouton // 2, y + hauteur_bouton // 2))
    fenetre.blit(texte_surface, texte_rect)

def afficher_texte(texte:str, x:int, y:int, couleur:tuple, font:str, taille_police=36, surface=fenetre):
    """
    Affiche du texte dans une fenêtre Pygame en respectant les retours à la ligne ('\n')
    et en coupant les lignes trop longues pour qu'elles restent dans la fenêtre.

    Cette fonction a été créée par notre professeur M.Maurice puis modifiée par Esteban ROUVIERE pour inclure une surface sur laquelle écrire, une police, une taille et un retour a la ligne si il y a un \n.

    Paramètres :
    -----------
        texte (str) : Le texte à afficher, peut contenir des retours à la ligne ('\n').

        x (int) : Position en pixels sur l'axe horizontal où commence le texte.

        y (int) : Position en pixels sur l'axe vertical où commence le texte.

        couleur (tuple) : Couleur du texte sous forme de tuple (R, G, B).

        taille_police (int) : Taille de la police (par défaut : 36).

        surface (pygame.Surface) : La surface sur laquelle on veut écrire.

    """
    font = pygame.font.Font(font, taille_police)
    texte = texte.upper()
    lignes = texte.split('\n')  # Séparation des lignes manuelles avec \n
    y_offset = 0  # Décalage vertical

    for ligne in lignes:
        mots = ligne.split(' ') #sépare les mots dans chaque lignes
        ligne_actuelle = ''

        for mot in mots:
            # Vérifie si on peut ajouter le mot sans dépasser la largeur
            if font.size(ligne_actuelle + mot)[0] <= surface.get_width() - x:
                ligne_actuelle += mot + ' '
            else:
                # Affiche la ligne et passe à la suivante
                surface.blit(font.render(ligne_actuelle.strip(), True, couleur), (x, y + y_offset))
                ligne_actuelle = mot + ' '
                y_offset += font.get_height()

        # Affiche la dernière ligne de cette section (ou si elle tient en une seule ligne)
        if ligne_actuelle:
            surface.blit(font.render(ligne_actuelle.strip(), True, couleur), (x, y + y_offset))
            y_offset += font.get_height()  # Décalage pour la ligne suivante

def leaving():
    """
    Cette fonction affiche un texte lorsque le joueur souhaite quitter

    Fonction créée par Louis SAINT-JEAN

    """
    fenetre.blit(sortie,(0,0))
    afficher_texte("Au plaisir de vous revoir", 50, 50, (255,255,255), "../data/polices/geoform/geoform.otf")
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    exit()
