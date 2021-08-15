from pgzero.builtins import Actor

explosionNames = ["impact_", "explosion_"]
explosionFrames = [8, 10]

class Explosion():
    def __init__(self, index, posX, posY):
        self.index = index
        self.actor = Actor(explosionNames[index]+"0", (posX, posY))
        self.imageIndex = 0
        self.frame = 0
    def draw(self):
        self.actor.draw()
    def update(self):
        self.frame += 1
        if 0 == self.frame % 6:
            self.imageIndex += 1
            if self.imageIndex < explosionFrames[self.index]:
                self.actor.image = explosionNames[self.index]+str(self.imageIndex)
            else:
                return False
        return True
    
class ExplosionList():
    def __init__(self):
        self.explosions = []
    def draw(self):
        for explosion in self.explosions:
            explosion.draw()
    def update(self):
        for i in reversed(range(len(self.explosions))):
            active = self.explosions[i].update()
            if not active:
                del self.explosions[i]
    def append(self, index, posX, posY):
        self.explosions.append(Explosion(index, posX, posY))
