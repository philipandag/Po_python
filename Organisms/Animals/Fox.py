from Organisms.Animals.Animal import Animal


class Fox(Animal):
    NAME = "Fox"
    SYMBOL = "F"
    COLOR = (255, 134, 0)
    STRENGTH = 3
    INITIATIVE = 7
    def __init__(self):
        super(Fox, self).__init__(Fox.NAME, Fox.SYMBOL, Fox.COLOR, Fox.STRENGTH, Fox.INITIATIVE)