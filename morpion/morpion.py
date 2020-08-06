#usr/bin/python
# -*- coding: utf-8 -*-


"""
    Morpion
    *************************************************************************
    Implémentation du Jeu Morpion avec un joueur contre une Intelligence Artificielle.
    *************************************************************************

"""

class Morpion:
    def __init__(self):
        self.game_table = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.ia_pion = ""
        self.player_pion = ""

        print("-------------------------------------------------------------------------------------------------------")
        print("\t Programmeur : DIALLO Mamadou")
        print("\t Langage De Programmation : Python")
        print("\t Étudiant : Master Informatique")
        print("\t Univeristé Grenoble Alpes : 2020")
        print("\t Intelligence Artificielle : Adapation du Jeux Morpion")
        print("\t Année : 2020")
        print("-------------------------------------------------------------------------------------------------------")

        print("\n\t Bienvenue ! Soyez de grands stratéges dans vos choix de  mouvement ! \n")


    # Choix des Pions de Morpion pour la partie de Jeu
    def choicePion(self):
        print("\n\t Si vous choisissez le pion X, c'est l'Intelligence Artificielle qui jouera en premier. \n")
        print("-------------------------------------------------------------------------------------------------------")
        # On demande au Joueur de choisir son Pion
        while(self.player_pion != "O" and self.player_pion != "X") :
            self.player_pion = input("\nChoisissez le pion X ou O : ").upper()
            # Dans ce cas c'est le Joueur qui débute la partie
            if self.player_pion == "O" :
                self.ia_pion ="X"
            else:
                self.ia_pion = "O"
                # L'IA donne joue son premier Coup
                self.playerIa()


    # Le jeu de l'IA
    def playerIa(self):
        # L'IA cherche d'abord une position gagnante (son meilleur coup)
        coup_morpion_ia = self.winningPosition(self.ia_pion)
        if coup_morpion_ia == 0 :
            # Ensuite l'IA vérifie que le joueur n'est pas en position de gagner
            coup_morpion_ia = self.winningPosition(self.player_pion)
            if coup_morpion_ia == 0 :
                # On vérifie que le centre de la matrice n'est pas occupée
                if self.game_table[5] == 5 :
                    coup_morpion_ia = 5     # L'IA occupe le centre de la matrice pour réduire les chances du joueur
                else:
                    # Le centre de la matrice est déjà occupé par le joueur
                    # L'IA cherche la première position libre
                    for i in range(10) :
                        if (self.game_table[i] == str(i)) :
                            coup_morpion_ia = i
                            break

        self.game_table[coup_morpion_ia] = self.ia_pion # L'IA place son pion
        print("\n IA : ","J'ai placé mon Pion à la position " + str(coup_morpion_ia))
        return



    # Le jeu du Joueur
    def player(self):
        """
        coup_morpion_player = 0
        while (coup_morpion_player <= 0 or coup_morpion_player > 9) :
            try:
                # Le joueur choisi l'emplacement de son Pion
                coup_morpion_player = int(input("Où est ce que vous placer votre Pion ? "))
                # On vérifie que la case choisi par le Joueur n'est pas occupée
                if self.game_table[coup_morpion_player] != coup_morpion_player :
                    print("La Case est déjà occupée, Rejouez svp ! ")
                    coup_morpion_player = 0
            except ValueError:
                coup_morpion_player = 0

        self.game_table[coup_morpion_player] = self.player_pion # Le Joueur place son pion
        print("Joueur : ", "J'ai placé mon Pion à la position " + str(coup_morpion_player))
        return
        """

        coup_morpion_player = 0
        while (coup_morpion_player <= 0 or coup_morpion_player > 9):
            coup_morpion_player = int(input("\n Où est-ce que vous placez votre pion ?  "))
            if self.game_table[coup_morpion_player] != str(coup_morpion_player):
                print("\nLa case est déja occupée, Rejouez svp !\n")
                coup_morpion_player = 0
        self.game_table[coup_morpion_player] = self.player_pion
        return


    # Gestion du déroulement du Jeu
    def playerTurn(self):
        current_games = True
        while (current_games) :
            self.displayGame()  # Affichage du Jeu à l'Écran
            self.player()       # Le Joueur joue
            if self.checkGameOver(self.player_pion) :   # On vérifie si le joueur a gagné ou non
                current_games = False
            else:
                self.displayGame()  # Affichage du Jeu à l'Écran
                self.playerIa()     # L'IA joue
                if self.checkGameOver(self.ia_pion):     # On vérifie si l'IA a gagné ou non
                    current_games = False



    # Detection de meilleurs coup pour l'IA
    def winningPosition(self, pion):
        if (self.game_table[2] == pion and self.game_table[3] == pion and self.game_table[1] == "1") :
            return 1
        if (self.game_table[4] == pion and self.game_table[7] == pion and self.game_table[1] == "1") :
            return 1
        if (self.game_table[5] == pion and self.game_table[9] == pion and self.game_table[1] == "1") :
            return 1

        if (self.game_table[1] == pion and self.game_table[3] == pion and self.game_table[2] == "2") :
            return 2
        if (self.game_table[5] == pion and self.game_table[8] == pion and self.game_table[2] == "2") :
            return 2

        if (self.game_table[1] == pion and self.game_table[2] == pion and self.game_table[3] == "3") :
            return 3
        if (self.game_table[5] == pion and self.game_table[7] == pion and self.game_table[3] == "3") :
            return 3
        if (self.game_table[6] == pion and self.game_table[9] == pion and self.game_table[3] == "3") :
            return 3

        if (self.game_table[5] == pion and self.game_table[6] == pion and self.game_table[4] == "4") :
            return 4
        if (self.game_table[1] == pion and self.game_table[7] == pion and self.game_table[4] == "4") :
            return 4

        if (self.game_table[1] == pion and self.game_table[9] == pion and self.game_table[5] == "5") :
            return 5
        if (self.game_table[2] == pion and self.game_table[8] == pion and self.game_table[5] == "5") :
            return 5
        if (self.game_table[4] == pion and self.game_table[6] == pion and self.game_table[5] == "5") :
            return 5
        if (self.game_table[3] == pion and self.game_table[7] == pion and self.game_table[5] == "5") :
            return 5

        if (self.game_table[4] == pion and self.game_table[5] == pion and self.game_table[6] == "6") :
            return 6
        if (self.game_table[3] == pion and self.game_table[9] == pion and self.game_table[6] == "6") :
            return 6

        if (self.game_table[1] == pion and self.game_table[4] == pion and self.game_table[7] == "7") :
            return 7
        if (self.game_table[3] == pion and self.game_table[5] == pion and self.game_table[7] == "7") :
            return 7
        if (self.game_table[8] == pion and self.game_table[9] == pion and self.game_table[7] == "7") :
            return 7

        if (self.game_table[2] == pion and self.game_table[5] == pion and self.game_table[8] == "8"):
            return 8
        if (self.game_table[7] == pion and self.game_table[9] == pion and self.game_table[8] == "8"):
            return 8

        if (self.game_table[1] == pion and self.game_table[5] == pion and self.game_table[9] == "9") :
            return 9
        if (self.game_table[3] == pion and self.game_table[6] == pion and self.game_table[9] == "9"):
            return 9
        if (self.game_table[7] == pion and self.game_table[8] == pion and self.game_table[9] == "9"):
            return 9

        return 0


    # On vérifie l'etat du jeu après chaque coup de chaque du joueur ou de l'IA pour savoir qui a gagné
    def checkGameOver(self, pion):
        if (
                (self.game_table[1] == pion and self.game_table[2] == pion and self.game_table[3] == pion)
                or (self.game_table[1] == pion and self.game_table[4] == pion and self.game_table[7] == pion)
                or (self.game_table[1] == pion and self.game_table[5] == pion and self.game_table[9] == pion)
                or (self.game_table[2] == pion and self.game_table[5] == pion and self.game_table[8] == pion)
                or (self.game_table[4] == pion and self.game_table[5] == pion and self.game_table[6] == pion)
                or (self.game_table[3] == pion and self.game_table[5] == pion and self.game_table[7] == pion)
                or (self.game_table[3] == pion and self.game_table[6] == pion and self.game_table[9] == pion)
                or (self.game_table[7] == pion and self.game_table[8] == pion and self.game_table[9] == pion)
        ) :
            if pion == self.player_pion :
                print("\n\tVous avez gagné contre l'Intelligence Artificielle ! BRAVO !\n")
            else:
                print("\n\tVous avez perdu ! ")
            return True
        else:
            for i in range(10) :
                if self.game_table[i] == str(i) :
                    return False
            print("\n\tMatch Nul ! ")
            return True


    # Affichage de chaque état du Jeu
    def displayGame(self):
        print("-------------")
        print("| " + self.game_table[1] + " | " + self.game_table[2] + " | " + self.game_table[3] + " |" )
        print("-------------")
        print("| " + self.game_table[4] + " | " + self.game_table[5] + " | " + self.game_table[6] + " |")
        print("-------------")
        print("| " + self.game_table[7] + " | " + self.game_table[8] + " | " + self.game_table[9] + " |")
        print("-------------")



# Début du Programme
if __name__ == "__main__":
    game = Morpion()
    game.choicePion()

    game.playerTurn()
    print("\n\tFin du Jeu\n")
    game.displayGame()


