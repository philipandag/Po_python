from Direction import Direction
from Field import Field

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
        self.alive = False
        self.pos = None

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
        self.alive = True
        self.pos = self.field.gridPos

    def alive(self):
        return self.alive

    def move_to(self, pos):
        self.field.set_organism(None)
        self.board.at(pos).set_organism(self)

    def action(self):
        direction = self.world.direction_class()
        direction.randomise()

        for i in range(direction.directions()):
            delta = direction.delta()
            pos = (self.pos[0] + delta[0], self.pos[1] + delta[1])
            if self.board.onBoard(pos):
                self.move_to(pos)
                return


