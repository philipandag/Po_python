import random

from Organisms.Animals.Animal import Animal


class Tortoise(Animal):
    NAME = "Tortoise"
    SYMBOL = "T"
    COLOR = (63, 134, 118)
    STRENGTH = 2
    INITIATIVE = 1
    MOVE_CHANCE = 0.25
    def __init__(self):
        super(Tortoise, self).__init__(Tortoise.NAME, Tortoise.SYMBOL, Tortoise.COLOR, Tortoise.STRENGTH, Tortoise.INITIATIVE)
        
    def action(self):
        if random.random() < self.MOVE_CHANCE:
            self.breed_cooldown_down()
        else:
            super(Tortoise, self).action()