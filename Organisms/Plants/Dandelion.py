import random
from Organisms.Plants.Plant import Plant


class Dandelion(Plant):
    NAME = "Dandelion"
    SYMBOL = "D"
    COLOR = (120, 180, 30)
    STRENGTH = 1
    def __init__(self):
        super(Dandelion, self).__init__(Dandelion.NAME, Dandelion.SYMBOL, Dandelion.COLOR, Dandelion.STRENGTH)

    def action(self):
        self.breed_cooldown_down()
        for i in range(3):
            if self.is_able_to_breed() and random.random() < self.PLANT_BREED_CHANCE:
                self.breed()
