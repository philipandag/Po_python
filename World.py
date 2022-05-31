from typing import Type

from Console import Console
from Organisms.Animals.Human import Human
from Organisms.Organism import Organism


class World:
    def __init__(self):
        self.organisms = []
        self.board = None
        self.choosenOrganism = Human
        self.console = None

    def set_board(self, board):
        self.board = board

    def get_board(self):
        return self.board

    def set_organism(self, organism, pos):

        if organism is not None:
            self.write_log("Postawiono " + organism.get_name())
        else:
            self.write_log("Usunieto " + self.board.getGrid()[pos[0]][pos[1]].get_organism().get_name())

        field = self.board.getGrid()[pos[0]][pos[1]]
        field.set_organism(organism)

    def get_choosen_organism(self) -> Type[Organism]:
        return self.choosenOrganism

    def set_choosen_organism(self, organism_class):
        self.choosenOrganism = organism_class

    def set_console(self, console: Console):
        self.console = console

    def write_log(self, log: str):
        if self.console is not None:
            self.console.write(log)
        else:
            print(log)

