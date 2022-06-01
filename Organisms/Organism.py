from Board import Board
from Direction import Direction
from Field import Field
import random


class Organism:
    def __init__(self, name, symbol,  color, strength, initiative, breed_cooldown):
        self.name = name
        self.symbol = symbol
        self.color = color
        self.strength = strength
        self.initiative = initiative
        self.world = None
        self.board: Board = None
        self.field: Field = None
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
        self.board = world.get_board()

    def set_field(self, field):
        self.field = field
        self.alive = True
        self.pos = self.field.gridPos

    def is_alive(self):
        return self.alive

    def get_strength(self):
        return self.strength

    def get_initiative(self):
        return self.initiative

    def move_to(self, pos):
        self.field.set_organism(None)
        self.board.at(pos).set_organism(self)

    def try_to_move_to(self, pos):
        print(self.get_name(), self.pos,  "goes to", pos)
        if not self.board.at(pos).is_empty():
            if self.board.at(pos).get_organism().collision(self):
                self.move_to(pos)
        else:
            self.move_to(pos)

    def kill(self):
        print(self.get_name(), self.pos,  "dies")
        self.alive = False
        self.field.set_organism(None)
        self.world.remove_organism(self)

    def is_able_to_breed(self):
        return self.breed_cooldown == 0

    def breed(self):
        direction = self.world.direction_class()
        direction.randomise()

        for i in range(direction.directions()):
            delta = direction.delta()
            pos = (self.pos[0] + delta[0], self.pos[1] + delta[1])
            if self.board.onBoard(pos) and self.board.at(pos).is_empty():
                child = self.__class__()
                self.world.add_organism(child)
                self.board.at(pos).set_organism(child)
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
            print(attacker.get_name(), attacker.get_pos(), "attacks", self.get_name(), self.get_pos())
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
        direction = self.world.direction_class()
        direction.randomise()

        for i in range(direction.directions()):
            delta = direction.delta()
            pos = (self.pos[0] + delta[0], self.pos[1] + delta[1])
            if self.board.onBoard(pos):
                self.try_to_move_to(pos)
                break
            direction.next()


    def get_pos(self):
        return self.field.gridPos

    def delta_strength(self, delta: int):
        self.strength += delta
