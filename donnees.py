#Commentaires??
import random
def listeMots():
    '''reourne un mot au hasard dans une liste
    pensez a modifier le nombreDeMots si ajout de mots '''
    a = ['igloo', 'poisson', 'matin',
         'bus', 'voiture', 'moto',
         'python', 'bateau', 'maison',
         'pendu', 'test', 'disque',
         'coucou', 'poison', 'liste']
    nombreDeMots = 14   # -1 car commence de 0
    return a[random.randint(0, nombreDeMots)]

def NbrofChances():
    chance = 8
    return chance
 
