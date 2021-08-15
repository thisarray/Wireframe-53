import pgzrun
from pygame import image, Color, Surface
import math

from Listing08_Foreground import Foreground
from Listing20_Enemy import Enemy, enemyNames, enemyPaths

# cursor LEFT and RIGHT: change path
# mouse up and down: change Y starting point
# mouse CLICK: add enemy, path, start Y, time to start
# SPACE: print list

foreground = Foreground()

class SpaceShip:
    def __init__(self):
        self.actor = Actor("spaceship", (0,300))
spaceship = SpaceShip()

class Bullets:
    def __init__(self):
        pass
    def append(self, a, b, c, d):
        pass
bullets = Bullets()

class EnemyList:
    def __init__(self):
        self.listEnemies = []
    def draw(self):
        for enemy in self.listEnemies:
            enemy.draw()
    def update(self):
        for i in reversed(range(len(self.listEnemies))):
            active = self.listEnemies[i].update(bullets, spaceship)
            if not active:
                del self.listEnemies[i]
    def AddElement(self, enemy, posY):
        self.listEnemies.append(Enemy(enemy, posY))

enemies = [Enemy(i, 0) for i in range(len(enemyNames))]
enemyList = EnemyList()

currentEnemy = 0
currentY = 300

listElements = []
globalTime = 0

def draw():
    screen.clear()
    foreground.draw()
    enemyList.draw()
    enemies[currentEnemy].draw()
    for i in range(1, len(enemyPaths[currentEnemy])):
        screen.draw.line((enemyPaths[currentEnemy][i-1][0], enemyPaths[currentEnemy][i-1][1] + currentY),
                         (enemyPaths[currentEnemy][i][0], enemyPaths[currentEnemy][i][1] + currentY), (255,255,255))

def update():
    global globalTime
    globalTime += 1
    foreground.update(globalTime)
    enemies[currentEnemy].translate(800-50, currentY)
    enemyList.update()

def on_mouse_down(pos, button):
    listElements.append([currentEnemy, currentY, globalTime])
    enemyList.AddElement(currentEnemy, currentY)
    
def on_mouse_move(pos):
    global currentY
    currentY = pos[1]

def on_key_down(key):
    global currentEnemy
    if key == keys.SPACE:
        print(str(listElements))
    elif key == keys.LEFT or key == keys.UP:
        currentEnemy = (currentEnemy - 1) % len(enemies)
    elif key == keys.RIGHT or key == keys.DOWN:
        currentEnemy = (currentEnemy + 1) % len(enemies)

pgzrun.go()
