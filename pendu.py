#Jeux du pendu

from donnees import *
from fonctions import *

print("##########################")
print("###### Jeu du pendu ######")
print("##########################")
print("############# By Clément #")
print(" ")


Name = input("Entrer votre nom : ")
Name = str(Name)

scoresJeu = uploadScores()  #Charge le dictionnaire de scores dans un fichier scores
a = AddPlayer(Name) #Ajoute le joueur si il n'existe pas


if a == 1:
    print('Bienvenue a toi ', Name, ', ton score est de 0')

else:
    b = ReturnScore(Name)
    print ('Bienvenue', Name, ', ton score est de ', b)

#Choix du mot

mot = listeMots()

motCache = ''
for lettres in mot: #Créer un mot avec des étoiles avec la meme longueur
                    #que le mot à deviner
    motCache = motCache + '*'

print('Mot à deviner : ', motCache)

lettreJoueur = input('Entrer une lettre :')
a = mot.find(lettreJoueur)
if a < 0:
    print('Il n\' a pas de ', lettreJoueur, 'dans le mot')
