import math

def PositionFromLength(path, length):
    totalLength = 0.0
    for i in range(1, len(path)):
        dx = path[i][0] - path[i-1][0]
        dy = path[i][1] - path[i-1][1]
        nextLength = math.sqrt(dx*dx + dy*dy)
        if length <= totalLength + nextLength:
            localParameter = (length - totalLength) / nextLength
            return True, (path[i-1][0] + localParameter * dx, path[i-1][1] + localParameter * dy)
        totalLength += nextLength
    return False, path[-1]

def Accelerate(path, length):
    length = length * length / 800
    return PositionFromLength(path, length)

def BigBossMovement(path, length):
    inPath, position = PositionFromLength(path, length)
    if inPath:
        return True, position
    totalLength = path[0][0] - path[1][0]
    return True, (position[0], 200*math.sin((length-totalLength)/40))

#enemyNames = ['ball', 'cannon', 'cannon_top', 'flying_saucer',
#              'rocket', 'ship_alien', 'ship_cannon', 'ship_fighter',
#              'ship_pistol', 'big_ship' ]

enemyMovement = [PositionFromLength, PositionFromLength, PositionFromLength, PositionFromLength,
                 Accelerate, PositionFromLength, PositionFromLength, PositionFromLength,
                 PositionFromLength, BigBossMovement ]
