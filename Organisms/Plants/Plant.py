from Organisms.Organism import Organism


class Plant(Organism):
    def __init__(self, name, symbol, color, strength):
        super(Plant, self).__init__(name, symbol, color, strength, 0)
