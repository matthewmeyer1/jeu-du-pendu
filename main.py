import random
import unidecode

# Fonction principal qui va etre appele par le code pour rouler le reste des fonctions
def principal():
    rejouer = True
    while rejouer:
        nbre_tours = 6
        mot_choisi, mot_actuel = choisir_mot()
        iteration_tours(mot_actuel, mot_choisi , nbre_tours)

        rejouer = recommancer()


# Fonction qui va selectionner un mot random de la liste et la retourner
def choisir_mot():
    with open("mots_pendu.txt", "r", encoding='utf-8') as mots_pendu:
        banque_de_mots = mots_pendu.readlines()

    mot_choisi = random.choice(banque_de_mots).strip('\n')
    mot_choisi = unidecode.unidecode(mot_choisi)
    mot_choisi = mot_choisi.lower()
    mot_actuel = "_" * len(mot_choisi)
    print(mot_choisi)
    return mot_choisi, mot_actuel

# Fonction qui va ajouter la logique du jeu et laisser le joueur jouer plusieurs tours
def iteration_tours(mot_actuel, mot_choisi, nbre_chances):
    while nbre_chances > 0 and mot_actuel.__contains__('_'):
        mot_actuel, nbre_chances = tour(mot_actuel, mot_choisi, nbre_chances)
    message_de_fin(mot_choisi, nbre_chances)

# Fonction du tour du joueur
def tour(mot_actuel, mot_choisi, nbre_chances):
    bonne_lettre = False

    lettre = input("Devinez une lettre: ").lower()
    while not lettre.isalpha() or not len(lettre) == 1:
        print("La lettre doit être un seul charactêre, et doit etre entre 'a' à 'z'")
        lettre = input("Devinez une lettre: ").lower()


    if lettre == "+":
        mot_actuel = indice(mot_actuel, mot_choisi, nbre_chances)
    else:
        for index in range(len(mot_choisi)):
            if mot_choisi[index] == lettre:
                mot_actuel = modifier_mot_actuel(mot_actuel, index, lettre)
                bonne_lettre = True

        if not bonne_lettre:
            nbre_chances -= 1
            print(f"La lettre ne fait pas partie du mot. Il vous reste {nbre_chances} chances")
        else:
            print(f"La lettre fait partie du mot!")

        if not bonne_lettre and nbre_chances == 1:

            mot_actuel = indice(mot_actuel, mot_choisi, nbre_chances)

    print(mot_actuel)
    return mot_actuel, nbre_chances


# Fonction qui va modifier le mot actual, dependamment de la lettre choisi et du mot aleatoire
def modifier_mot_actuel(mot_actuel, index, lettre):
    return mot_actuel[:index] + lettre + mot_actuel[index + 1:]

# Fonction additionelle pour permettre au joueur un indice
def indice(mot_actuel, mot_choisi, nbre_chances):
    demande_indice = input("Voulez-vous un indice? (y/n)   ")
    demande_indice = demande_indice.lower()
    if demande_indice == "y" or demande_indice == "yes" or demande_indice == "oui":
        nbre_lettres_restants = mot_actuel.count("_")
        index_rand = random.randint(0, nbre_lettres_restants - 1)

        for index in range(len(mot_choisi)):
            if mot_actuel[index] == '_':
                index_rand -= 1
            if index_rand <= 0 and mot_actuel[index] == '_':
                lettre = mot_choisi[index]


                for index2 in range(len(mot_choisi)):
                    if mot_choisi[index2] == lettre:
                        mot_actuel = modifier_mot_actuel(mot_actuel, index2, lettre)

                break



    return mot_actuel


# Fonction qui va retourner soit une reussite du jeu ou un echec, et le dire au joueur
def message_de_fin(mot_choisi, nbre_chances):
    if nbre_chances == 0:
        print(f"Vous avez perdu :( Le mot était {mot_choisi}")
    else:
        print("Vous avez gagné!!! Félicitation :)")

def recommancer():
    restart = input("Voulez-vous rejouer? (y/n)   ")
    restart = restart.lower()
    if restart == "y" or restart == "yes" or restart == "oui":
        return True
    else:
        return False

principal()