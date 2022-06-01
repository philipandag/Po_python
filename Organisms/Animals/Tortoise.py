from Organisms.Animals.Animal import Animal


class Tortoise(Animal):
    NAME = "Tortoise"
    SYMBOL = "T"
    COLOR = (63, 134, 118)
    STRENGTH = 2
    INITIATIVE = 1
    def __init__(self):
        super(Tortoise, self).__init__(Tortoise.NAME, Tortoise.SYMBOL, Tortoise.COLOR, Tortoise.STRENGTH, Tortoise.INITIATIVE)