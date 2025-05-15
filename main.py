
# Fonction principal qui va etre appele par le code pour rouler le reste des fonctions
def principal():
    return 0

# Fonction qui va selectionner un mot random de la liste et la retourner
def choisir_mot():
    mot_choisi = ""
    mot_actuel = ""
    return mot_choisi, mot_actuel

# Fonction qui va reduire le nombre de chances restant
def reduire_nbre_chances_restant(nbre_chances):
    return nbre_chances - 1

# Fonction qui va retourner soit une reussite du jeu ou un echec, et le dire au joueur
def message_de_fin(nbre_chances):
    return 0

# Fonction qui va modifier le mot actual, dependamment de la lettre choisi et du mot aleatoire
def modifier_mot_actuel(mot_actuel, mot_fini, lettre):
    return mot_actuel

# Fonction qui va ajouter la logique du jeu et laisser le joueur jouer plusieurs tours
def iteration_tours(nbre_tours = 6):
    return 0