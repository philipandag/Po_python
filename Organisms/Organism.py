


class Organism:
    def __init__(self, name, symbol,  color, strength, initiative):
        self.name = name
        self.symbol = symbol
        self.color = color
        self.strength = strength
        self.initiative = initiative
        self.world = None
        self.board = None
        self.field = None

    def get_colour(self):
        return self.color

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def set_world(self, world):
        self.world = world
        self.board = world.get_board()

    def set_field(self, field):
        self.field = field
