from pgzero.builtins import Actor
from shapely.geometry import Polygon
from shapely.affinity import translate


shipName = 'spaceship'
shipPolyCoords = [(-48, -5), (4, -9), (10, -3), (40, 1), (19, 5), (-1, 5), (-1, 18), (-37, 18)]

class SpaceShip:
    def __init__(self):
        self.actor = Actor(shipName, (100,300))
        self.centredPolygon = Polygon(shipPolyCoords)
        self.polygon = translate(self.centredPolygon, self.actor.x, self.actor.y)
        self.numberOfLasers = 1
        self.vulnerable = True
        self.lastHit = 0
        self.numberOfLives = 3
    def draw(self):
        if self.vulnerable:
            self.actor.draw()
        elif self.lastHit < 120 and 0 == (self.lastHit // 3) % 2:
            self.actor.draw()
    def update(self):
        if not self.vulnerable:
            self.lastHit -= 1
            if self.lastHit == 0:
                self.vulnerable = True
    def translate(self, dispX, dispY):
        self.actor.x += dispX
        self.actor.y += dispY
        if self.actor.x < 45:
            self.actor.x = 45
        elif self.actor.x > 800-48:
            self.actor.x = 800-48
        if self.actor.y < 9:
            self.actor.y = 9
        elif self.actor.y > 600-18:
            self.actor.y = 600-18
        self.polygon = translate(self.centredPolygon, self.actor.x, self.actor.y)
    def shootLaser(self, lasers):
        if self.numberOfLives != 0 and self.lastHit < 120:
            startY = (self.numberOfLasers - 1) / 2 * 10
            for i in range(self.numberOfLasers):
                lasers.addLaser((self.actor.x + 20, self.actor.y+2 - startY + i * 10))
    def hit(self, explosions, showScore):
        if self.vulnerable:
            self.numberOfLives -= 1
            showScore.update(self.numberOfLives)
            self.lastHit = 180
            self.numberOfLasers = 1
            explosions.append(1, self.actor.x, self.actor.y)
            self.actor.x = 100
            self.actor.y = 300
            self.polygon = translate(self.centredPolygon, self.actor.x, self.actor.y)
            self.vulnerable = False
