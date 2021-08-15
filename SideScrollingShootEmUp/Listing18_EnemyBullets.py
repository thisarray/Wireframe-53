import math
from random import randint

def NoBullets(bullets, spaceShip, posX, posY, length, speed):
    pass

def BulletToSpaceship(bullets, spaceShip, posX, posY, speed):
    dx = spaceShip.actor.x - posX
    dy = spaceShip.actor.y - posY
    distance = math.sqrt(dx*dx + dy*dy)
    if distance > 20:
        bullets.append(posX, posY, dx / distance * (speed+3.0), dy / distance * (speed+3.0))

def SomeBulletsToSpaceship(bullets, spaceShip, posX, posY, length, speed):
    if 0 == randint(0,300):
        BulletToSpaceship(bullets, spaceShip, posX, posY, speed)

def MoreBulletsToSpaceship(bullets, spaceShip, posX, posY, length, speed):
    if 0 == randint(0,100):
        BulletToSpaceship(bullets, spaceShip, posX, posY, speed)

def BulletsBigBoss(bullets, spaceShip, posX, posY, length, speed):
    if length < 360:
        MoreBulletsToSpaceship(bullets, spaceShip, posX, posY, length, speed)
        MoreBulletsToSpaceship(bullets, spaceShip, posX, posY, length, speed)
    else:
        if 0 == round(length*2) % 50:
            for i in range(0, 360, 20):
                bullets.append(posX, posY, 3.0 * math.sin(i / 180.0 * math.pi), 3.0 * math.cos(i / 180.0 * math.pi))
        elif 0 == round(length*2) % 71:
            for i in range(0, 360, 10):
                bullets.append(posX, posY, 3.0 * math.sin(i / 180.0 * math.pi), 3.0 * math.cos(i / 180.0 * math.pi))

#enemyNames = ['ball', 'cannon', 'cannon_top', 'flying_saucer',
#              'rocket', 'ship_alien', 'ship_cannon', 'ship_fighter',
#              'ship_pistol', 'big_ship' ]

bulletStrategy = [NoBullets, MoreBulletsToSpaceship, MoreBulletsToSpaceship, SomeBulletsToSpaceship,
                  NoBullets, NoBullets, MoreBulletsToSpaceship, MoreBulletsToSpaceship,
                  MoreBulletsToSpaceship, BulletsBigBoss ]
