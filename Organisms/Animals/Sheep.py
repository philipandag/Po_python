from Organisms.Animals.Animal import Animal


class Sheep(Animal):
    NAME = "Sheep"
    SYMBOL = "S"
    COLOR = (189, 188, 199)
    STRENGTH = 4
    INITIATIVE = 4
    def __init__(self):
        super(Sheep, self).__init__(Sheep.NAME, Sheep.SYMBOL, Sheep.COLOR, Sheep.STRENGTH, Sheep.INITIATIVE)