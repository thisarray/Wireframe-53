from pgzero.builtins import Actor

class ShowScore():
    def __init__(self, number):
        self.ship = Actor("lives", (37, 20))
        self.number1 = Actor("text_0", (80, 20))
        self.number2 = Actor("text_"+str(number), (108, 20))
    def draw(self):
        self.ship.draw()
        self.number1.draw()
        self.number2.draw()
    def update(self, number):
        self.number2.image = "text_"+str(number)
