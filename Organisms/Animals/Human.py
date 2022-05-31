from Organisms.Animals.Animal import Animal


class Human(Animal):
    NAME = "Human"
    SYMBOL = "H"
    COLOR = (180, 20, 200)
    STRENGTH = 5
    INITIATIVE = 4
    def __init__(self):
        super(Human, self).__init__(Human.NAME, Human.SYMBOL, Human.COLOR, Human.STRENGTH, Human.INITIATIVE)