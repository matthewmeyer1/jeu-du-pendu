# Le code est le jeu du pendu codé par Matthew Meyer
# Le joueur peut choisir son propre fichier de mots
# Il y a 6 chances
# Un indice peut etre donné sil reste seulement 1 chance

import random
import os.path
import unicodedata


# Fonction principal qui va etre appele par le code pour rouler le reste des fonctions
def main():
    # loop pour pouvoir rejouer sans recommancer le programme
    rejouer = True
    while rejouer:
        nbre_tours = 6 # nombre de tours prédifini

        # Fonctions assurant le deroulement du jeu
        message_de_debut()
        mot_choisi, mot_actuel = choisir_mot() # Choix random du mot et creation du mot actuel
        iteration_tours(mot_actuel, mot_choisi , nbre_tours) # Partie principale du code, va iterer les tours

        rejouer = recommancer()

# Message d'explication du jeu
def message_de_debut():
    print("Bienvenue au jeu du pendu! Vous avez 6 chances pour deviner le mot")

# Fonction qui va selectionner un mot random de la liste et la retourner
def choisir_mot():

    # Demander le nom du fichier voulu
    liste_custom = input("Entrez le nom du fichier qui contient les mots (vide sera la liste défaut): ")

    # Si le fichier contient .txt, l'enlever pour
    liste_custom = liste_custom.replace(".txt", "")
    nom_de_fichier = ""

    if os.path.isfile(liste_custom + ".txt"): # Si le nom de fichier existe
        nom_de_fichier = liste_custom + ".txt"
    else: # Si le fichier existe pas
        print("Le fichier 'mots_pendu.txt' sera utilisé")
        nom_de_fichier = "mots_pendu.txt"

    with open(nom_de_fichier, "r", encoding='utf-8') as mots_pendu: # Ouvrir le fichier et creer une liste banque de mots
        banque_de_mots = mots_pendu.readlines()

    mot_choisi = random.choice(banque_de_mots).strip('\n') # Choisir un mot de la liste et Enlever le charactere de nouvelle ligne
    mot_choisi = ''.join(c for c in unicodedata.normalize('NFD', mot_choisi)
                  if unicodedata.category(c) != 'Mn') # Enlever les charactere speciaux tel que les accents
    mot_choisi = mot_choisi.lower() # S'assurer que tous les lettres du mot sont en minuscules
    mot_actuel = "_" * len(mot_choisi) # Creer le mot actual de la meme longueur du mot choisi, compose seulement de "_"

    return mot_choisi, mot_actuel

# Fonction qui va ajouter la logique du jeu et laisser le joueur jouer plusieurs tours
def iteration_tours(mot_actuel, mot_choisi, nbre_chances):
    while nbre_chances > 0 and mot_actuel.__contains__('_'): # Verifier quil reste des chances et que le mot na pas ete completement devine
        mot_actuel, nbre_chances = tour(mot_actuel, mot_choisi, nbre_chances) # Faire le tour, et changer le mot actual et le nombres de chances restantent si necessaire

    message_de_fin(mot_choisi, nbre_chances) # Afficher le message de fin

# Fonction du tour du joueur
def tour(mot_actuel, mot_choisi, nbre_chances):
    bonne_lettre = False # Variable qui va etre utilise pour determiner si la lettre choisie est dans le mot

    lettre = input("Devinez une lettre: ").lower() # Demander a l'utilisateur de choisir une lettre, et la mettre en minuscule

    # Verifier que la lettre est valide, sinon, redemander de choisir la lettre
    while not lettre.isalpha() or not len(lettre) == 1:
        print("La lettre doit être un seul charactêre, et doit etre entre 'a' à 'z'")
        lettre = input("Devinez une lettre: ").lower()


    # Iterer sur les characteres du mot choisi pour voir si la lettre choisie correspond
    for index in range(len(mot_choisi)):
        if mot_choisi[index] == lettre: # Le charactere du mot est egal a la lettre
            mot_actuel = modifier_mot_actuel(mot_actuel, index, lettre) # Modification du mot actuel en ajoutant la lettre au bon index
            bonne_lettre = True # La lettre est valide


    if not bonne_lettre: # Enlever une chance si la lettre nest pas presente dans le mot
        nbre_chances -= 1
        print(f"La lettre ne fait pas partie du mot. Il vous reste {nbre_chances} chances")
    else:
        print(f"La lettre fait partie du mot!")


    if not bonne_lettre and nbre_chances == 1: # Sil reste une chance, donner l'indice
        mot_actuel = indice(mot_actuel, mot_choisi, nbre_chances)


    print(mot_actuel) # Imprimer l'etat du mot devine apres le tour
    return mot_actuel, nbre_chances

# Fonction qui va modifier le mot actual, dependamment de la lettre choisi et du mot aleatoire
def modifier_mot_actuel(mot_actuel, index, lettre):
    return mot_actuel[:index] + lettre + mot_actuel[index + 1:] # Envoyer le nouveau mot actuel, qui a recu une lettre a un index specifique

# Fonction additionelle pour permettre au joueur un indice
def indice(mot_actuel, mot_choisi, nbre_chances):
    demande_indice = input("Voulez-vous un indice? (y/n)   ")  # Demander a l'utilisateur sil veut un indice
    demande_indice = demande_indice.lower()

    if demande_indice == "y" or demande_indice == "yes" or demande_indice == "oui": # Sil veut un indice
        nbre_lettres_restants = mot_actuel.count("_") # Voir combien de lettre il reste a deviner
        index_rand = random.randint(0, nbre_lettres_restants - 1) # Du nombre de lettres restant, prendre un chiffre random pour donner en indice

        # Iterer chaque charactere du mot actual
        for index in range(len(mot_actuel)):
            if mot_actuel[index] == '_': # Si le charactere est '_', enlever 1 de l'index
                index_rand -= 1
            if index_rand <= 0 and mot_actuel[index] == '_': # Si lindex est rendu a 0, cest le temps de donner lindice et la lettre
                lettre = mot_choisi[index] # la lettre choisi est a lindex du mot choisi

                # Puisque la lettre de lindice peut figurer plusieurs fois dans le mot, une deuxieme loop est cree pour mettre a jour toutes les instances de la lettre
                for index2 in range(len(mot_choisi)):
                    if mot_choisi[index2] == lettre:
                        mot_actuel = modifier_mot_actuel(mot_actuel, index2, lettre)
                break

    return mot_actuel

# Fonction qui va retourner soit une reussite du jeu ou un echec, et le dire au joueur
def message_de_fin(mot_choisi, nbre_chances):
    if nbre_chances == 0: # Sil reste 0 chances, l'utilisateur a perdu
        print(f"Vous avez perdu :( Le mot était {mot_choisi}")
    else: # sinon, il a gagne
        print("Vous avez gagné!!! Félicitations :)")

def recommancer():
    restart = input("Voulez-vous rejouer? (y/n)   ") # Demande si le joueur veut rejouer
    restart = restart.lower()

    # Envoyer un boolean True ou False sil veut rejouer ou pas
    if restart == "y" or restart == "yes" or restart == "oui":
        return True
    else:
        return False





main() # Appeler la fonction principale