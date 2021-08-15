import pgzrun
import math
from random import randint
from shapely.geometry import Polygon
from Listing10_Bullets import AllBullets
bullets = AllBullets()
for i in range(700):
    speed = randint(1,3)
    angle = randint(0,359) / 180 * math.pi
    bullets.append(randint(0,800),randint(0,600), speed*math.sin(angle), speed*math.cos(angle))
def draw():
    screen.clear()
    bullets.draw()
def update():
    bullets.update()
    bullets.collide(Polygon([(350,250),(450,250),(450,350),(350,350)]))
pgzrun.go()
