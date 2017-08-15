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
