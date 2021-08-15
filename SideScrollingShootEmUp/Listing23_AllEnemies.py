from shapely.affinity import translate

from Listing20_Enemy import Enemy
from Listing22_MapEnemyStart import enemyStart

class EnemyList:
    def __init__(self):
        self.listEnemies = []
        self.nextEnemyIndex = 0
        self.allPolygons = []
    def draw(self):
        for enemy in self.listEnemies:
            enemy.draw()
    def update(self, globalTime, bullets, spaceShip):
        for i in reversed(range(len(self.listEnemies))):
            active = self.listEnemies[i].update(bullets, spaceShip)
            if not active:
                del self.listEnemies[i]
        if self.nextEnemyIndex < len(enemyStart):
            if globalTime >= enemyStart[self.nextEnemyIndex][2]:
                self.listEnemies.append(Enemy(enemyStart[self.nextEnemyIndex][0], enemyStart[self.nextEnemyIndex][1]))
                self.nextEnemyIndex += 1
        self.allPolygons = []
        for enemy in self.listEnemies:
            polygon = translate(enemy.polygon, enemy.actor.x, enemy.actor.y)
            self.allPolygons.append(polygon)
    def destroyEnemy(self, index, explosions):
        explosions.append(1, self.listEnemies[index].actor.x, self.listEnemies[index].actor.y)
        del self.listEnemies[index]
        del self.allPolygons[index]
    def laserHit(self, index, powerups, explosions):
        destroyed = self.listEnemies[index].hit(powerups)
        if destroyed:
            self.destroyEnemy(index, explosions)
