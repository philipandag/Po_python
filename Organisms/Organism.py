from SquareBoard import SquareBoard
from Direction import Direction
from Field import Field
import random
from abc import ABC


class Organism(ABC):
    def __init__(self, name, symbol,  color, strength, initiative, breed_cooldown):
        self.name = name
        self.symbol = symbol
        self.color = color
        self.strength = strength
        self.initiative = initiative
        self.world = None
        self.alive = False
        self.pos = None
        self.MAX_BREED_COOLDOWN = breed_cooldown
        self.breed_cooldown = breed_cooldown

    def get_colour(self):
        return self.color

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def set_world(self, world):
        self.world = world

    def set_field(self, field):
        self.alive = True
        self.pos = field.gridPos

    def is_alive(self):
        return self.alive

    def get_strength(self):
        return self.strength

    def get_initiative(self):
        return self.initiative

    def move_to(self, pos):
        self.world.get_board().at(self.pos).set_organism(None)
        self.world.get_board().at(pos).set_organism(self)
        self.pos = pos

    def try_to_move_to(self, pos):
        print(self.get_name(), self.pos,  "goes to", pos)
        if not self.get_board().at(pos).is_empty():
            if self.get_board().at(pos).get_organism().collision(self):
                self.move_to(pos)
        else:
            self.move_to(pos)

    def kill(self):
        print(self.get_name(), self.pos,  "dies")
        self.alive = False
        self.get_field().set_organism(None)
        self.world.remove_organism(self)

    def is_able_to_breed(self):
        return self.breed_cooldown == 0

    def breed(self):
        direction = self.world.get_direction()()
        direction.randomise()

        for i in range(direction.directions()):
            delta = direction.delta()
            pos = (self.pos[0] + delta[0], self.pos[1] + delta[1])
            if self.get_board().onBoard(pos) and self.get_board().at(pos).is_empty():
                child = self.__class__()
                self.world.add_organism(child)
                self.get_board().at(pos).set_organism(child)
                print("new", child.get_name(), "born at", child.get_pos())
                break
            direction.next()
        self.breed_cooldown = self.MAX_BREED_COOLDOWN

    # return True allows attacker to go on self's pos
    def collision(self, attacker) -> bool:
        if self.get_name() == attacker.get_name():
            print(attacker.get_name(), attacker.get_pos(), "meets with", self.get_name(), self.get_pos())
            if self.is_able_to_breed() and attacker.is_able_to_breed():
                print(attacker.get_name(), attacker.get_pos(), "breeds with", self.get_name(), self.get_pos())
                self.breed()
            else:
                if not self.is_able_to_breed():
                    print(self.get_name(), self.get_pos(), "is not able to breed")
                if not attacker.is_able_to_breed():
                    print(attacker.get_name(), attacker.get_pos(), "is not able to breed")
            return False
        else:
            print(attacker.get_name(), attacker.get_pos(), "strength", attacker.get_strength(), "attacks", self.get_name(), self.get_pos(), "strength", self.get_strength())
            if self.get_strength() < attacker.get_strength():
                self.kill()
                return True
            else:
                attacker.kill()
                return False

    def breed_cooldown_down(self):
        if self.breed_cooldown > 0:
            self.breed_cooldown -= 1

    def action(self):
        direction = self.world.get_direction()()
        direction.randomise()

        for i in range(direction.directions()):
            delta = direction.delta()
            pos = (self.pos[0] + delta[0], self.pos[1] + delta[1])
            if self.get_board().onBoard(pos):
                self.try_to_move_to(pos)
                break
            direction.next()
        self.breed_cooldown_down()


    def get_pos(self):
        return self.get_field().gridPos

    def delta_strength(self, delta: int):
        self.strength += delta

    def get_board(self):
        return self.world.get_board()

    def get_field(self):
        return self.world.get_board().at(self.pos)
