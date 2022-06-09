from Organisms.Animals.Animal import Animal


class Wolf(Animal):
    NAME = "Wolf"
    SYMBOL = "W"
    COLOR = (72, 82, 80)
    STRENGTH = 9
    INITIATIVE = 5

    def __init__(self):
        super(Wolf, self).__init__(Wolf.NAME, Wolf.SYMBOL, Wolf.COLOR, Wolf.STRENGTH, Wolf.INITIATIVE)
