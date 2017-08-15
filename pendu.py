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
