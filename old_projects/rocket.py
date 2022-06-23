from math import sqrt
from random import randint

class Rocket:
    nextId = 1
    def __init__(self, speed=1, altitude = 0, x = 0, name=''):
        self.altitude = altitude
        self.speed = speed
        self.x = x
        self.name = name
        self.id = Rocket.nextId
        Rocket.nextId += 1

    def moveUp(self):
        """opis naszej klasy
        """
        self.altitude += self.speed
    
    def get_distance(self, rocket):
        ab = (rocket.altitude - self.altitude) ** 2
        bc = (rocket.x - self.x) ** 2
        return sqrt(ab + bc)

    def __str__(self):
        return "Actual altitude of rocket is: " + str(self.altitude) + "\n" + "Actual x is: " + str(self.x)

class RocketBoard:
    def __init__(self, amountOfRockets = 5):   
        self.rockets = [Rocket(randint(1, 4), x = randint(0, 5)) for _ in range(amountOfRockets)]

        for _ in range(10):
            drawnedRocket = randint(0, len(self.rockets) - 1)
            self.rockets[drawnedRocket].moveUp()

        for rocket in self.rockets:
            print(rocket)
    def __getitem__(self, key):
        return self.rockets[key]
    
    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

    @staticmethod
    def get_distance(rocket1: Rocket, rocket2: Rocket) -> float:
        ab = (rocket2.altitude - rocket1.altitude) ** 2
        bc = (rocket2.x - rocket1.x) ** 2
        return sqrt(ab + bc)
