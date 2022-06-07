from Organisms.Organism import Organism
import random


class Plant(Organism):
    PLANT_BREED_COOLDOWN = 3
    PLANT_STRENGTH = 0
    PLANT_BREED_CHANCE = 0.1

    def __init__(self, name, symbol, color, strength):
        super(Plant, self).__init__(name, symbol, color, strength, self.PLANT_STRENGTH, self.PLANT_BREED_COOLDOWN)

    def action(self):
        self.breed_cooldown_down()
        if self.is_able_to_breed() and random.random() < self.PLANT_BREED_CHANCE:
            self.breed()
