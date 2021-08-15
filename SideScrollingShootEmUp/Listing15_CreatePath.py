import pgzrun
import pygame
import math

lines = [[]]
currentLine = 0

def addCosinus(scale, numberOfWaves):
    global currentLine
    steps = 810 // 10
    for i in range(steps + 2):
        lines[currentLine].append((800 - i*10, round(300 + scale * math.cos(numberOfWaves * i / steps * math.pi))))
    currentLine += 1
    lines.append([])

for i in range(1, 5):
    addCosinus(100, i)
for i in range(1, 5):
    addCosinus(-100, i)

def addLoop(scaleX, scaleY, numberOfWaves):
    global currentLine
    steps = 810 // 10
    for i in range(steps):
        lines[currentLine].append((round(800 - i*10 + scaleX * math.sin(numberOfWaves * i / steps * math.pi)),
                                   round(300 + scaleY * math.cos(numberOfWaves * i / steps * math.pi))))
    currentLine += 1
    lines.append([])

addLoop(-200, 200, 5)
addLoop(-200, 200, 2)
addLoop(-200, -200, 5)
addLoop(-200, -200, 2)

usePoint = False
lastPoint = (0,0)

def draw():
    screen.clear()
    for i in range(1, len(lines[currentLine])):
        screen.draw.line(lines[currentLine][i-1], lines[currentLine][i], (255,255,255))
    if usePoint and len(lines[currentLine]) > 0:
        screen.draw.line(lines[currentLine][len(lines[currentLine])-1], lastPoint, (255,255,255))

def update():
    pass

def on_mouse_down(pos, button):
    global usePoint, lastPoint
    usePoint = True
    lastPoint = pos

def on_mouse_up(pos):
    global usePoint
    lines[currentLine].append(pos)
    usePoint = False
    
def on_mouse_move(pos):
    global lastPoint
    lastPoint = pos

def on_key_down(key):
    global currentLine
    if key == keys.SPACE:
        linesAtZero = [[(lines[j][i][0], lines[j][i][1] - lines[j][0][1]) for i in range(len(lines[j]))] for j in range(len(lines))]
        print(str(linesAtZero))
    elif len(lines[currentLine]) > 0 and (key == keys.BACKSPACE or key == keys.DELETE):
        lines[currentLine].pop(len(lines[currentLine]) - 1)
    elif key == keys.LEFT:
        currentLine = (currentLine - 1) % len(lines);
    elif key == keys.RIGHT:
        currentLine = (currentLine + 1) % len(lines)
    elif key == keys.PLUS or key == keys.KP_PLUS:
        currentLine = len(lines)
        lines.append([])

pgzrun.go()

