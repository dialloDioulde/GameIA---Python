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

    def __init__(self, niveau):
        self.step = 1
        self.hour = 0
        self.gravitation = 100

        if niveau == 1 :
            self.spatialship = Spatialship(5000, 1000, 5000, 200, 500)
        elif niveau == 2 :
            self.spatialship = Spatialship(6000, 2000, 4000, 400, 600)
        else:
            self.spatialship = Spatialship(8000, 3000, 7000, 300, 700)

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

    niveau = 0
    while (niveau < 1 or niveau > 3) :
        try:
            niveau = int(input("Indiquez le niveau du Jeu (1 ou 2 ou 3) : "))
        except ValueError:
            niveau = 1

    game = Landing(niveau)
    message = "C'est parti"
    while game.inFlit():
        game.showSpatialship(message)
        game.piloting()
        message = game.simulation()

    game.showSpatialship(message)
    game.result()





