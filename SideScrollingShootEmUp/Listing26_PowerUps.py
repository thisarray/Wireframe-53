from pgzero.builtins import Actor

class PowerUps():
    def __init__(self):
        self.powerups = []
    def draw(self):
        for powerup in self.powerups:
            powerup.draw()
    def update(self):
        for i in reversed(range(len(self.powerups))):
            self.powerups[i].x -= 1
            if self.powerups[i].x < -16:
                del self.powerups[i]
    def append(self, posX, posY):
        self.powerups.append(Actor("plus", (posX, posY)))
