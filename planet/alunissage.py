#usr/bin/python
# -*- coding: utf-8 -*-


class Spatialship():

    def __init__(self):
        self.altitude = 5000
        self.speed = 1000
        self.fuel = 1000
        self.push = 0
        self.pushMax = 500

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
        self.fuel -= fuel
        if self.fuel < 0 :
            self.fuel = 0

    def setPush(self, push):
        self.push = push

    def setPushMax(self, push):
        self.pushMax = push




class Landing():

    def __init__(self):
        self.step = 1
        self.hour = 0
        self.gravitation = 100
        self.spatialship = Spatialship()
        print("L\'altitude du Viasseau en orbite est {}".format(self.spatialship.getAltitude()))

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
        push = - 1
        while (push < 0 or push > self.spatialship.getPushMax()):
            try:
                push = int(input("\nQuelle Quantité de Carburant doit être Consommée (max = {:<3}) ? ".format(self.spatialship.getPushMax())))
            except ValueError :
                push = 0

        self.spatialship.burnFuel(push)
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
    message = "C'est parti"
    while game.inFlit():
        game.showSpatialship(message)
        game.piloting()
        message = game.simulation()

    game.showSpatialship(message)
    game.result()





