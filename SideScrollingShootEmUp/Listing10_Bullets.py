from pgzero.builtins import Actor
from shapely.geometry import Point
class Bullet:
    def __init__(self, pos, speed):
        self.actor = Actor('bullet', pos)
        self.speed = speed
    def update(self):
        self.actor.x += self.speed[0]
        self.actor.y += self.speed[1]
    def draw(self):
        self.actor.draw()
class AllBullets:
    def __init__(self):
        self.bullets = []
    def update(self):
        for i in reversed(range(len(self.bullets))):
            self.bullets[i].update()
            if self.bullets[i].actor.x < -4 or self.bullets[i].actor.y < -4 or self.bullets[i].actor.x > 804 or self.bullets[i].actor.y > 604:
                del self.bullets[i]
    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
    def append(self, posX, posY, velX, velY):
        self.bullets.append(Bullet((posX, posY), (velX, velY)))
    def collide(self, polygon):
        collided = False
        for i in reversed(range(len(self.bullets))):
            if Point(self.bullets[i].actor.x, self.bullets[i].actor.y).within(polygon):
                collided = True
                del self.bullets[i]
        return collided
