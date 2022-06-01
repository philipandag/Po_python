from typing import Type

from Console import Console
from DirectionSquare import DirectionSquare
from Organisms.Animals.Human import Human
from Organisms.Organism import Organism


class World:
    def __init__(self):
        self.organisms = []
        self.board = None
        self.choosenOrganism = Human
        self.console = None
        self.turn_counter = 0;
        self.direction_class = DirectionSquare

    def set_board(self, board):
        self.board = board

    def get_board(self):
        return self.board

    def set_organism(self, organism, pos):

        if organism is not None:
            print("Postawiono " + organism.get_name())
        else:
            print("Usunieto " + self.board.getGrid()[pos[0]][pos[1]].get_organism().get_name())

        field = self.board.getGrid()[pos[0]][pos[1]]
        field.set_organism(organism)

    def get_choosen_organism(self) -> Type[Organism]:
        return self.choosenOrganism

    def set_choosen_organism(self, organism_class):
        self.choosenOrganism = organism_class


    def next_turn(self):
        print("Turn " + str(self.turn_counter))
        for organism in self.organisms:
            if organism.alive():
                organism.action()
        self.turn_counter += 1

