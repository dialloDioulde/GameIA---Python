#usr/bin/python
# -*- coding: utf-8 -*-


class Spatialship():

    def __init__(self, altitude, speed, fuel, push, pushMax):
        self.altitude = altitude
        self.speed = speed
        self.fuel = fuel
        self.push = push
        self.pushMax = pushMax

    def getAltitude(self):
        return self.altitude

    def getSpeed(self):
        return self.speed

    def getFuel(self):
        return self.fuel

    def getPush(self):
        return self.push

    def getPushMax(self):
        return self.pushMax

    def setAltitude(self, altitude):
        if altitude < 0 :
            altitude = 0
        self.altitude = altitude

    def setSpeed(self, speed):
        self.speed = speed

    def setFuel(self, fuel):
        self.fuel = fuel

    def burnFuel(self, fuel):
        if fuel > self.fuel :
            fuel = self.fuel
        self.fuel -= fuel

        push = (self.push // 2 + fuel) // 2
        return push

    def setPush(self, push):
        self.push = push

    def setPushMax(self, push):
        self.pushMax = push




class Landing():

    def __init__(self):
        self.step = 1
        self.hour = 0
        self.gravitation = 100
        self.levels = {
            'Facile': [
                1, # Numéro du Niveau
                5000, # Altitude de Départ
                1200, # Vitesse Initiale
                4000, # Carburant Initiale
                300, # Quantité de Carburant à Consommer
                500, # Quantité de Carburant Maximale à Consommer
            ],
            'Moyen': [
                2,
                6000,
                2000,
                4000,
                400,
                600
            ],
            'Difficile': [
                3,
                8000,
                3000,
                7000,
                300,
                700
            ]
        }

    def levelChoice(self):
        print("\nListe des Niveaux de Jeu Disponibles : ")
        for level in self.levels:
            print("\t{} - {}".format(self.levels[level][0], level))

        levelGame = 0
        while (levelGame < 1 or levelGame > len(self.levels)) :
            try:
                levelGame = int(input("Indiquez le niveau du Jeu 1/{} : ".format(len(self.levels))))
            except ValueError :
                levelGame = 1

        for level in self.levels:
            if self.levels[level][0] == levelGame :
                altitude = self.levels[level][1]
                speed = self.levels[level][2]
                fuel = self.levels[level][3]
                push = self.levels[level][4]
                pushMax = self.levels[level][5]
                self.spatialship = Spatialship(altitude, speed, fuel, push, pushMax)
                break


        print("\nL\'altitude du Viasseau en orbite est {}".format(self.spatialship.getAltitude()))

    def inFlit(self):
        if self.spatialship.getAltitude() > 0 :
            return True
        else:
            return False

    def showSpatialship(self, message):
        print("\t+-------------------------------------+")
        print("\t|************** Étapte {:>2} ************|".format(self.step))
        print("\t+-------------------------------------+")
        if self.spatialship.getFuel() <= 0 :
            print("\t| {:^36}|".format("Niveau de Carburant FAIBLE !!"))
            print("\t+-------------------------------------+")
        print("\t|  {:^34} |".format(message))
        print("\t+-------------------------------------+")
        print("\t| L'Altitude {:>5} m   Carburant {:>5}|".format(self.spatialship.getAltitude(), self.spatialship.getFuel()))
        print("\t| Vitesse {:>5} m/s    Poussée {:>5}  |".format(self.spatialship.getSpeed(), self.spatialship.getPush()))
        print("\t+-------------------------------------+")


    def piloting(self):
        fuel = - 1
        while (fuel < 0 or fuel > self.spatialship.getPushMax()):
            try:
                fuel = int(input("\nQuelle Quantité de Carburant doit être Consommée (max = {:<3}) ? ".format(self.spatialship.getPushMax())))
            except ValueError :
                fuel = 0

        push = self.spatialship.burnFuel(fuel)
        self.spatialship.setPush(push)

    def simulation(self):
        self.step += 1

        speed = self.spatialship.getSpeed() + self.gravitation - self.spatialship.getPush()
        altitudeStart = self.spatialship.getAltitude()
        altitudeNow = altitudeStart - speed

        self.spatialship.setAltitude(altitudeNow)
        self.spatialship.setSpeed(speed)

        if altitudeNow > altitudeStart :
            msg = " Le Vaisseau monte ! "
        elif altitudeNow == altitudeStart :
            msg = " Le Vaisseau est en Statinonnement ! "
        else:
            msg = " Le Vaisseau descend ! "

        return msg


    def result(self):
        speed = self.spatialship.getSpeed()
        if speed > 100:
            print("Le Vaisseau Spatial s'est écrasé, il n'y a pas de survivant !")
        elif speed > 30 :
            print("\n Le Vaisseau Spatial s'est posé brutalement, il y'au un problème ! ")
        else:
            print("\n Féliciation, Mise en Orbite Réussie !")
        print("\n Fin du Jeu !")



if __name__ == "__main__":
    print("Alunissage")
    print("*" *20, "\n")


    game = Landing()
    game.levelChoice()

    message = "C'est parti"
    while game.inFlit():
        game.showSpatialship(message)
        game.piloting()
        message = game.simulation()

    game.showSpatialship(message)
    game.result()





