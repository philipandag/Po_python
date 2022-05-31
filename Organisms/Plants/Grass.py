from Organisms.Plants.Plant import Plant


class Grass(Plant):
    NAME = "Grass"
    SYMBOL = "g"
    COLOR = (20, 180, 30)
    STRENGTH = 1
    def __init__(self):
        super(Grass, self).__init__(Grass.NAME, Grass.SYMBOL, Grass.COLOR, Grass.STRENGTH)
