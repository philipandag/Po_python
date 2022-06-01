from Organisms.Animals.Animal import Animal


class Antelope(Animal):
    NAME = "Antelope"
    SYMBOL = "A"
    COLOR = (249, 231, 83)
    STRENGTH = 4
    INITIATIVE = 4
    def __init__(self):
        super(Antelope, self).__init__(Antelope.NAME, Antelope.SYMBOL, Antelope.COLOR, Antelope.STRENGTH, Antelope.INITIATIVE)