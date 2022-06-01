from Organisms.Organism import Organism


class Plant(Organism):
    PLANT_BREED_COOLDOWN = 3
    PLANT_STRENGTH = 0
    def __init__(self, name, symbol, color, strength):
        super(Plant, self).__init__(name, symbol, color, strength, self.PLANT_STRENGTH, self.PLANT_BREED_COOLDOWN)

    def action(self):
        pass
