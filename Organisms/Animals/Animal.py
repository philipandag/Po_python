from Organisms.Organism import Organism


class Animal(Organism):
    ANIMAL_BREED_COOLDOWN = 3
    def __init__(self, name, symbol, color, strength, initiative):
        super(Animal, self).__init__(name, symbol, color, strength, initiative, self.ANIMAL_BREED_COOLDOWN)