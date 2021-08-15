import pgzrun
import Listing01_Background as background
globalFrameCount = 0
def draw():
    background.draw(screen, globalFrameCount)
def update():
    global globalFrameCount
    globalFrameCount += 1
pgzrun.go()
