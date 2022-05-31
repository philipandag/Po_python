from Organisms.Organism import Organism


class Animal(Organism):
    def __init__(self, name, symbol, color, strength, initiative):
        super(Animal, self).__init__(name, symbol, color, strength, initiative)