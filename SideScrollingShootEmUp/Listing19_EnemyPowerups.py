
def NoPowerup(powerups, posX, posY):
    pass

def AddPowerup(powerups, posX, posY):
    powerups.append(posX, posY)

#enemyNames = ['ball', 'cannon', 'cannon_top', 'flying_saucer',
#              'rocket', 'ship_alien', 'ship_cannon', 'ship_fighter',
#              'ship_pistol', 'big_ship' ]

powerUpStrategy = [AddPowerup, NoPowerup, NoPowerup, NoPowerup,
                   NoPowerup, NoPowerup, NoPowerup, NoPowerup,
                   NoPowerup, NoPowerup ]
