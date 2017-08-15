#Commentaires??
import random
def listeMots():
    '''reourne un mot au hasard dans une liste
    pensez a modifier le nombreDeMots si ajout de mots '''
    a = ['igloo', 'poisson', 'matin', 'bus', 'voiture', 'moto', 'python', 'bateau', 'maison', 'pendu']
    nombreDeMots = 10
    return a[random.randint(0, nombreDeMots)]

def NbrofChances():
    chance = 8
    return chance
