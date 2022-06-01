from typing import Type

from Console import Console
from DirectionSquare import DirectionSquare
from Organisms.Animals.Human import Human
from Organisms.Organism import Organism
from Board import Board


class World:
    def __init__(self):
        self.organisms = []
        self.to_add = []
        self.board: Board = None
        self.chosenOrganism = Human
        self.console = None
        self.turn_counter = 0;
        self.direction_class = DirectionSquare

    def set_board(self, board):
        self.board = board

    def get_board(self):
        return self.board

    def add_organism(self, organism):
        organism.set_world(self)
        self.add_organism_sorted(organism)

    def add_organism_sorted(self, organism):
        added = False
        for i in range(len(self.organisms)):
            if self.organisms[i].get_initiative() < organism.get_initiative():
                self.organisms.insert(i, organism)
                added = True
        if not added:  # didnt found any organism slower than organism
            self.organisms.append(organism)

    def add_organisms(self):
        for organism in self.to_add:
            self.add_organism_sorted(organism)
        self.to_add.clear()

    def remove_organism(self, organism):
        self.organisms.remove(organism)

    def set_organism(self, organism, pos):
        field = self.board.at(pos)
        if organism is not None:
            print("Placed", organism.get_name(), "on", pos)
            self.add_organism(organism)
        else:
            print("Deleted", self.board.at(pos).get_organism().get_name())
            self.remove_organism(field.organism)

        field.set_organism(organism)

    def get_choosen_organism(self) -> Type[Organism]:
        return self.chosenOrganism

    def set_choosen_organism(self, organism_class):
        self.chosenOrganism = organism_class


    def next_turn(self):
        print("Turn:", self.turn_counter)
        #self.add_organisms()
        for organism in self.organisms:
            if organism.is_alive():
                organism.action()
        self.turn_counter += 1

    def get_to_add_list(self):
        return self.to_add

