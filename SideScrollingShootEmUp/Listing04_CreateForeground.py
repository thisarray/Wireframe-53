import pgzrun
from pygame import image, Color, Surface

from Listing03_ForegroundNames import foregroundNames

foregroundTiles = [Actor(name) for name in foregroundNames]
foreground = []
currentForeground = 0
currentPosition = (0,0)
currentX = 0

def draw():
    screen.clear()
    for tile in foreground:
        tile.draw()
    foregroundTiles[currentForeground].draw()

def update(dt):
    foregroundTiles[currentForeground].pos = currentPosition

def on_mouse_down(pos, button):
    global currentForeground
    if mouse.LEFT == button:
        foreground.append(Actor(foregroundNames[currentForeground], currentPosition))
    elif mouse.RIGHT == button:
        currentForeground = (currentForeground + 1) % len(foregroundNames)

def on_mouse_move(pos):
    global currentPosition
    currentPosition = pos

def on_key_down(key):
    global currentX, currentForeground
    if key == keys.LEFT and currentX > 0:
        currentX -= 100
        for tile in foreground:
            tile.pos = (tile.pos[0] + 100, tile.pos[1])
    elif key == keys.RIGHT:
        currentX += 100
        for tile in foreground:
            tile.pos = (tile.pos[0] - 100, tile.pos[1])
    elif key == keys.UP:
        currentForeground = (currentForeground + 1) % len(foregroundNames)
    elif key == keys.DOWN:
        currentForeground = (currentForeground + len(foregroundNames) - 1) % len(foregroundNames)
    elif key == keys.SPACE:
        foreground.sort(key = lambda tile: tile.pos[0] + currentX)
        for tile in foreground:
            print("("+str(foregroundNames.index(tile.image))+","+
                  str(round(tile.pos[0] + currentX))+","+
                  str(round(tile.pos[1]))+"),")

pgzrun.go()
