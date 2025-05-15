import random
import unidecode

# Fonction principal qui va etre appele par le code pour rouler le reste des fonctions
def principal():
    nbre_tours = 6
    mot_choisi, mot_actuel = choisir_mot()
    iteration_tours(mot_actuel, mot_choisi , nbre_tours)

# Fonction qui va selectionner un mot random de la liste et la retourner
def choisir_mot():
    with open("mots_pendu.txt", "r", encoding='utf-8') as mots_pendu:
        banque_de_mots = mots_pendu.readlines()

    mot_choisi = random.choice(banque_de_mots).strip('\n')
    mot_choisi = unidecode.unidecode(mot_choisi)
    mot_actuel = "_" * len(mot_choisi)

    return mot_choisi, mot_actuel

# Fonction qui va ajouter la logique du jeu et laisser le joueur jouer plusieurs tours
def iteration_tours(mot_actuel, mot_choisi, nbre_chances):
    while nbre_chances > 0 and mot_actuel.__contains__('_'):
        mot_actuel, nbre_chances = tour(mot_actuel, mot_choisi, nbre_chances)
    message_de_fin(mot_choisi, nbre_chances)

# Fonction du tour du joueur
def tour(mot_actuel, mot_choisi, nbre_chances):
    bonne_lettre = False
    lettre = input("Devinez une lettre: ")

    for index in range(len(mot_choisi)):
        if mot_choisi[index] == lettre:
            mot_actuel = modifier_mot_actuel(mot_actuel, index, lettre)
            bonne_lettre = True

    if not bonne_lettre:
        nbre_chances -= 1
        print(f"Il vous reste {nbre_chances} chances")

    print(mot_actuel)
    return mot_actuel, nbre_chances


# Fonction qui va modifier le mot actual, dependamment de la lettre choisi et du mot aleatoire
def modifier_mot_actuel(mot_actuel, index, lettre):
    return mot_actuel[:index] + lettre + mot_actuel[index + 1:]



# Fonction qui va retourner soit une reussite du jeu ou un echec, et le dire au joueur
def message_de_fin(mot_choisi, nbre_chances):
    if nbre_chances == 0:
        print(f"Vous avez perdu :( Le mot était {mot_choisi}")
    else:
        print("Vous avez gagné!!! Félicitation :)")

principal()