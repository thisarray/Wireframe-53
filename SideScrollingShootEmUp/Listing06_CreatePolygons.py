import pgzrun
from pygame import image, Color, Surface

from Listing03_ForegroundNames import foregroundNames as imageNames
#from Listing12_EnemyNames import enemyNames as imageNames
#imageNames = ['spaceship']

images = [Actor(imageNames[i], (800//2, 600//2)) for i in range(len(imageNames))]
lines = [[] for i in range(len(imageNames))]
currentImage = 0
usePoint = False
lastPoint = (0,0)

def draw():
    screen.clear()
    images[currentImage].draw()
    for i in range(1, len(lines[currentImage])):
        screen.draw.line(lines[currentImage][i-1], lines[currentImage][i], (255,255,255))
    if usePoint and len(lines[currentImage]) > 0:
        screen.draw.line(lines[currentImage][len(lines[currentImage])-1], lastPoint, (255,255,255))

def update():
    pass

def on_mouse_down(pos, button):
    global usePoint, lastPoint
    usePoint = True
    lastPoint = pos

def on_mouse_up(pos):
    global usePoint
    lines[currentImage].append(pos)
    usePoint = False
    
def on_mouse_move(pos):
    global lastPoint
    lastPoint = pos

def on_key_down(key):
    global currentImage
    if key == keys.SPACE:
        displacedLines = [[(lines[i][j][0] - 400, lines[i][j][1] - 300) for j in range(len(lines[i]))] for i in range(len(lines))]
        print(str(displacedLines)+",")
    elif len(lines[currentImage]) > 0 and (key == keys.BACKSPACE or key == keys.DELETE):
        lines[currentImage].pop(len(lines[currentImage]) - 1)
    elif key == keys.LEFT:
        currentImage = (currentImage - 1) % len(imageNames);
    elif key == keys.RIGHT:
        currentImage = (currentImage + 1) % len(imageNames);

pgzrun.go()

