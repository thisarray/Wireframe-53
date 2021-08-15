import pgzrun
from enum import Enum

isFastComputer = True
if isFastComputer:
    import Listing01_Background as background
from Listing08_Foreground import Foreground
from Listing10_Bullets import AllBullets
from Listing23_AllEnemies import EnemyList, enemyStart
from Listing24_SpaceShip import SpaceShip
from Listing25_Lasers import Lasers
from Listing26_PowerUps import PowerUps
from Listing27_ShowScore import ShowScore
from Listing28_Explosions import ExplosionList
import Listing29_Collisions as collisions

foreground = Foreground()
bullets = AllBullets()
enemyList = EnemyList()
spaceShip = SpaceShip()
lasers = Lasers()
powerups = PowerUps()
showScore = ShowScore(spaceShip.numberOfLives)
explosions = ExplosionList()

Status = Enum('Status', 'PLAYING GAME_OVER LEVEL_CLEAR')
gameStatus = Status.PLAYING
globalTime = 0

def draw():
    if isFastComputer:
        background.draw(screen, globalTime)
    else:
        screen.clear()
    foreground.draw()
    enemyList.draw()
    if gameStatus != Status.GAME_OVER:
        spaceShip.draw()
    powerups.draw()
    lasers.draw()
    bullets.draw()
    explosions.draw()
    showScore.draw()
    if gameStatus == Status.GAME_OVER:
        screen.draw.text("GAME OVER", center=(400, 260), fontsize=55, color=(255,0,0))
    elif gameStatus == Status.LEVEL_CLEAR:
        screen.draw.text("LEVEL CLEAR", center=(400, 260), fontsize=55, color=(0,0,255))

def update():
    global globalTime, gameStatus
    globalTime += 1
    bullets.update()
    lasers.update()
    powerups.update()
    foreground.update(globalTime)
    enemyList.update(globalTime, bullets, spaceShip)
    if gameStatus != Status.GAME_OVER:
        if keyboard.left:  spaceShip.translate(-4,  0)
        if keyboard.right: spaceShip.translate( 4,  0)
        if keyboard.up:    spaceShip.translate( 0, -4)
        if keyboard.down:  spaceShip.translate( 0,  4)
    spaceShip.update()
    explosions.update()
    collisions.collisionBulletsForeground(bullets, foreground, explosions)
    collisions.collisionLaserForeground(lasers, foreground, explosions)
    collisions.collisionLaserEnemies(lasers, enemyList, explosions, powerups)
    if gameStatus == Status.PLAYING:
        collisions.collisionShipBullets(bullets, spaceShip, explosions, showScore)
        collisions.collisionShipForeground(spaceShip, foreground, explosions, showScore)
        collisions.collisionShipEnemies(spaceShip, enemyList, explosions, showScore, powerups)
        collisions.collisionShipPowerUps(spaceShip, powerups)
        if spaceShip.numberOfLives == 0:
            gameStatus = Status.GAME_OVER
        elif globalTime > enemyStart[-1][2] + 10 and len(enemyList.listEnemies) == 0:
            gameStatus = Status.LEVEL_CLEAR

def on_key_down(key):
    if key == keys.SPACE:
        spaceShip.shootLaser(lasers)
        
pgzrun.go()
