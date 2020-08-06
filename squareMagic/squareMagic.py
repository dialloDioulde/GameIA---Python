#usr/bin/python
# -*- coding: utf-8 -*-


"""
    Carrés magiques
    *************************************************************************
    Ce programme génère des carrés magiques de taille quelconque mais impaire
    en utilisant la méthode diagonale.
    Un carré magique est un carré de nombres dans lequel les sommes des
    nombres de chaque rangée, de chaque colonne et des deux diagonales sont
    égales.
    L'ordinateur demande la taille, seuls les nombres impairs sont acceptés.
    *************************************************************************

"""


# Choix de la taille du Carré par l'utilisateur
def squareDimension():
    square_dimension = 0
    print("Choisissez la taille du Carré : ")
    while (square_dimension % 2 == 0):
        square_dimension = int(input("Entrez un nombre Impair ==>  "))
        print("\n")
    print("Calcul d'un Carré de {}x{} ".format(square_dimension, square_dimension))
    return square_dimension


n = squareDimension()

# Initialisation Du Carré sous forme de liste avec des 0 au début
array = [[ 0 for i in range(n)] for j in range(n)]

# Initialisation De l'Alogrithme
i, j = n, (n + 1) // 2

# Initialisation de la case contenant le 1 au début l'exécution de l'algorithme
array[i - 1][j - 1] = 1

# Boucle : Pour compléter les valeurs manquantes du carré de (2 à n**2 + 1)
for k in range(2, n**2 + 1):
    # Test avec le critère i+1 et j+1 par (modul n)
    i2 = (i + 1) % n    # On définit l'indice i2
    j2 = (j + 1) % n    # On définit l'indice j2

    if array[i2 - 1][j2 - 1] == 0 :     # La case est vide donc on l'utilise
        i, j = i2, j2       # On affecte respectivement les valeurs i2, j2 aux indices i et j

        print("Etape", "*" *10, k)
        #Affichage de chaque état du Carré Magique avant le résultat final
        for row in array:
            print('  '.join("{}".format(k) for k in row))

    # Si la case est déjà remplie, on utilise la case i-1 et j
    else:
        i = (i - 1) % n         # On recalcule l'indice i
    array[i - 1][j - 1] = k     # Remplissage de la case

# Affichage et Vérification des sommes par ligne et colonne
print("\n")
print("*" *10, "Résultat Final", "*" *10)
print("Carré Magique d'Ordre {} :".format(n))
for row in array:
    print('  '.join("{:2d}".format(k) for k in row), '=', sum(row))
print('  '.join('==' for k in row))
print('  '.join(str(sum(array[i][j] for i in range(n))) for j in range(n)))









