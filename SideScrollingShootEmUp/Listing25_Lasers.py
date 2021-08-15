from pgzero.builtins import Actor

class Lasers:
    def __init__(self):
        self.allLasers = []
    def draw(self):
        for laser in self.allLasers:
            laser.draw()
    def update(self):
        for i in reversed(range(len(self.allLasers))):
            self.allLasers[i].x += 20
            if self.allLasers[i].x > 800+10:
                del self.allLasers[i]
    def addLaser(self, position):
        self.allLasers.append(Actor('laser', position))
