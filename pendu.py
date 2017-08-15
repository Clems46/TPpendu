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



i = NbrofChances()
coup = 0
MotTrouve = 0


    
while MotTrouve >= 0 and coup < NbrofChances():
        
    print('Mot à deviner : ', motCache)
    lettreJoueur = input('Entrer une lettre :')
    a = mot.find(lettreJoueur)
    if a < 0:
        print('Il n\' a pas de {} dans le mot'.format(lettreJoueur))
        coup += 1
        print('Coup restant : {} / {}'.format(coup, NbrofChances()))

    else :
        print("Bien")
        print("")

        while a >= 0 & a <= len(mot):      #Boucle qui permet d'ajouter plusieurs lettres identiques du meme mots           
            motCache = ModifyString(motCache, a, lettreJoueur)
            a += 1
            a = mot.find(lettreJoueur, a, len(mot))
                
    MotTrouve = motCache.find('*')      #Cherche des étoiles dans le mot cachés
#afin de checker si le mot est trouvé

if MotTrouve < 0:
    print('Trouvé !!')
if coup >= i:
    print('Perdu !!!')


