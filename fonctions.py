#Fonctions du pendu

import pickle

def save(scoresJeu):
    """Enregistre l'objet 'scoresJeu' dans un fichier binaire
'scores' et renvoi 1 ou 0 si ça fonctionne ou pas"""
    a = 0
    with open('scores', 'wb') as fichier:
        monPickler = pickle.Pickler(fichier)
        monPickler.dump(scoresJeu)
        a = 1
        return a

def uploadScores():
    """Renvoie le fichier de scores"""
    with open('scores', 'rb') as fichier:
        monDepickler = pickle.Unpickler(fichier)
        scoreRecup = monDepickler.load()
        return scoreRecup
def NameExist(Name):
    """Retourne 1 si le nom existe et 0 si il n'exixte pas"""
    with open('scores', 'rb') as fichier:
        monDepickler = pickle.Unpickler(fichier)
        scoreRecup = monDepickler.load()
#Pas complet

def ReturnScore(Name):
    """Retourne le score du joueur Name"""
    with open('scores', 'rb') as fichier:
        monDepickler = pickle.Unpickler(fichier)
        scoreRecup = monDepickler.load()
    return scoreRecup[Name]
