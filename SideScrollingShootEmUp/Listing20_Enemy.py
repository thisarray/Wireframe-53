from pgzero.builtins import Actor
from shapely.geometry import Polygon

from Listing12_EnemyNames import enemyNames
from Listing13_EnemyPolygons import enemyPolyCoords
from Listing14_EnemyHits import enemyNumberOfHits
from Listing16_EnemyPaths import enemyPaths, enemySpeeds
from Listing17_EnemyMovements import enemyMovement
from Listing18_EnemyBullets import bulletStrategy
from Listing19_EnemyPowerups import powerUpStrategy

class Enemy:
    def __init__(self, index, startY):
        self.index = index
        self.startY = startY
        self.actor = Actor(enemyNames[index], (800+200,startY))
        self.actorWhite = Actor(enemyNames[index]+"_white", (800+200,startY))
        self.positionInPath = 0.0
        self.polygon = Polygon(enemyPolyCoords[index])
        self.numberOfHits = enemyNumberOfHits[index]
        self.lastHit = 0
    def draw(self):
        if self.lastHit == 0:
            self.actor.draw()
        else:
            self.actorWhite.draw()
            self.lastHit -= 1
    def translate(self, posX, posY):
        self.actor.x = self.actorWhite.x = posX
        self.actor.y = self.actorWhite.y = posY
    def update(self, bullets, spaceShip):
        self.positionInPath += enemySpeeds[self.index]
        active, position = enemyMovement[self.index](enemyPaths[self.index], self.positionInPath)
        if active:
            self.translate(position[0], position[1] + self.startY)
            bulletStrategy[self.index](bullets, spaceShip, position[0], position[1] + self.startY, self.positionInPath, enemySpeeds[self.index])   
        return active
    def hit(self, powerups):
        self.numberOfHits -= 1
        if self.numberOfHits <= 0:
            powerUpStrategy[self.index](powerups, self.actor.x, self.actor.y)
            return True
        self.lastHit = 5
        return False
