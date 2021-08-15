import pgzrun
from Listing08_Foreground import Foreground
foreground = Foreground()
globalTime = 0
def draw():
    foreground.draw()
def update():
    global globalTime
    globalTime += 1
    foreground.update(globalTime)
pgzrun.go()
