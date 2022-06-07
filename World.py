from typing import Type

from Console import Console
from DirectionSquare import DirectionSquare
from Organisms.Animals.Human import Human
from Organisms.Organism import Organism
from Board import Board
from Organisms.Plants.PineBorscht import PineBorscht


class World:
    def __init__(self, game, dimensions):
        self.organisms = []
        self.to_add = []
        self.chosenOrganism = Human
        self.console = None
        self.turn_counter = 0
        self.game = game
        self.organism_listeners = []
        self.dimensions = dimensions
        self.to_remove = []

    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes['game']
        return attributes

    def add_organism(self, organism):
        organism.set_world(self)
        self.add_organism_sorted(organism)

    def add_organism_sorted(self, organism):
        added = False
        for i in range(len(self.organisms)):
            if self.organisms[i].get_initiative() < organism.get_initiative():
                self.organisms.insert(i, organism)
                added = True
                break
        if not added:  # didnt found any organism slower than organism
            self.organisms.append(organism)

    def add_organisms(self):
        for organism in self.to_add:
            self.add_organism_sorted(organism)
        self.to_add.clear()

    def remove_organism(self, organism):
        self.to_remove.append(organism)
        if organism in self.organism_listeners:
            self.remove_listener(organism)

    def remove_organism_immediately(self, organism):
        self.organisms.remove(organism)
        if organism in self.organism_listeners:
            self.remove_listener(organism)

    def set_organism(self, organism, pos):
        field = self.game.board.at(pos)
        if organism is not None:
            print("Placed", organism.get_name(), "on", pos)
            self.add_organism(organism)
        else:
            print("Deleted", self.game.board.at(pos).get_organism().get_name(), "on", self.game.board.at(pos).get_organism().get_pos())
            self.remove_organism_immediately(field.organism)

        field.set_organism(organism)

    def get_chosen_organism(self) -> Type[Organism]:
        return self.chosenOrganism

    def set_chosen_organism(self, organism_class):
        self.chosenOrganism = organism_class

    def next_turn(self):
        if not hasattr(self, 'to_remove'):
            self.to_remove = []

        for o in self.to_remove:
            self.organisms.remove(o)
        self.to_remove.clear()

        print("Turn:", self.turn_counter, "Organisms: ", len(self.organisms))
        for organism in self.organisms:
            if organism.is_alive():
                organism.action()
            else:
                self.to_remove.append(organism)

        for o in self.to_remove:
            self.organisms.remove(o)
        self.to_remove.clear()

        self.turn_counter += 1

    def get_to_add_list(self):
        return self.to_add

    def add_listener(self, listener):
        self.organism_listeners.append(listener)

    def remove_listener(self, listener):
        self.organism_listeners.remove(listener)

    def get_board(self):
        return self.game.board

    def get_direction(self):
        return self.get_board().get_direction()
