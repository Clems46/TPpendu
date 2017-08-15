#!/usr/local/bin/python3.6
# -*-coding:Utf-8 -*

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
    try:
        with open('scores', 'rb') as fichier:
            monDepickler = pickle.Unpickler(fichier)
            scoreRecup = monDepickler.load()
            return scoreRecup
    except FileNotFoundError:
        save({})
        
    
def NameExist(Name):
    """Retourne 1 si le nom existe et 0 si il n'exixte pas"""
    try:
        a = uploadScores()
        if Name in a.keys():
            b = 1
        else:
            b = 0
        return b
    except FileNotFoundError:
       save({}) 

def ReturnScore(Name):
    """Retourne le score du joueur Name"""
    with open('scores', 'rb') as fichier:
        monDepickler = pickle.Unpickler(fichier)
        scoreRecup = monDepickler.load()
    return scoreRecup[Name]

def AddPlayer(Name):
    a = NameExist(Name)
    c = 0
    if a == 0:
        print("Ajout d'un nouveau joueur ")
        b = uploadScores()
        b[Name] = 0
        save(b)
        c = 1
        return c
    else:
        c = 0
        return c
def changeScores(Name, score):
    a = uploadScores()
    a[Name] = score
    b = save(a)
    return b

def ModifyString(word, position, letter):
    """Remplace une lettre du mot word à la position
position par la lettre letter"""
    
    i = 0
    a =[]
    
    for element in word:
        a.append(word[i])
        i += 1
    a[position] = letter
    return "".join(a)

