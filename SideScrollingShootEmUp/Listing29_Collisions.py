from shapely.geometry import Point, Polygon, LineString
from shapely.affinity import translate

def collisionShipBullets(bullets, spaceShip, explosions, showScore):
    if bullets.collide(spaceShip.polygon):
        spaceShip.hit(explosions, showScore)

def collisionBulletsForeground(bullets, foreground, explosions):
    for i in reversed(range(len(bullets.bullets))):
        for poly in foreground.polygons:
            point = Point(bullets.bullets[i].actor.x, bullets.bullets[i].actor.y)
            if point.within(poly):
                explosions.append(0, point.x, point.y)
                del bullets.bullets[i]
                break

def collisionLaserForeground(lasers, foreground, explosions):
    for j in reversed(range(len(lasers.allLasers))):
        laserLine = LineString([(lasers.allLasers[j].x - 26, lasers.allLasers[j].y),
                                (lasers.allLasers[j].x + 26, lasers.allLasers[j].y)])
        for i in reversed(range(len(foreground.polygons))):
            if not laserLine.disjoint(foreground.polygons[i]):
                explosions.append(0, lasers.allLasers[j].x + 26, lasers.allLasers[j].y)
                del lasers.allLasers[j]
                break

def collisionLaserEnemies(lasers, enemyList, explosions, powerups):
    for j in reversed(range(len(lasers.allLasers))):
        laserLine = LineString([(lasers.allLasers[j].x - 26, lasers.allLasers[j].y),
                                (lasers.allLasers[j].x + 26, lasers.allLasers[j].y)])
        for i in reversed(range(len(enemyList.allPolygons))):
            if not laserLine.disjoint(enemyList.allPolygons[i]):
                explosions.append(0, lasers.allLasers[j].x + 26, lasers.allLasers[j].y)
                enemyList.laserHit(i, powerups, explosions)
                del lasers.allLasers[j]
                break

def collisionShipPolygons(spaceShip, polygons):
    for i in reversed(range(len(polygons))):
        if not spaceShip.polygon.disjoint(polygons[i]):
            return True, i
    return False, 0
    
def collisionShipForeground(spaceShip, foreground, explosions, showScore):
    hit, index = collisionShipPolygons(spaceShip, foreground.polygons)
    if hit:
        spaceShip.hit(explosions, showScore)
    
def collisionShipEnemies(spaceShip, enemyList, explosions, showScore, powerups):
    hit, index = collisionShipPolygons(spaceShip, enemyList.allPolygons)
    if hit:
        spaceShip.hit(explosions, showScore)
        enemyList.laserHit(index, powerups, explosions)

def collisionShipPowerUps(spaceShip, powerups):
    for i in reversed(range(len(powerups.powerups))):
        polygon = Polygon([(powerups.powerups[i].x-16, powerups.powerups[i].y-16),
                           (powerups.powerups[i].x-16, powerups.powerups[i].y+16),
                           (powerups.powerups[i].x+16, powerups.powerups[i].y+16),
                           (powerups.powerups[i].x+16, powerups.powerups[i].y-16)])
        if not spaceShip.polygon.disjoint(polygon):
            spaceShip.numberOfLasers += 1
            del powerups.powerups[i]
