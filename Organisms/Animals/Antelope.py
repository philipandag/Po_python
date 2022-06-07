import random

from Organisms.Animals.Animal import Animal


class Antelope(Animal):
    NAME = "Antelope"
    SYMBOL = "A"
    COLOR = (249, 231, 83)
    STRENGTH = 4
    INITIATIVE = 4
    ESCAPE_CHANCE = 0.5
    def __init__(self):
        super(Antelope, self).__init__(Antelope.NAME, Antelope.SYMBOL, Antelope.COLOR, Antelope.STRENGTH, Antelope.INITIATIVE)

    def action(self):
        direction = self.world.get_direction()()
        direction.randomise()

        for i in range(direction.directions()):
            delta = direction.delta()
            pos = (self.pos[0] + delta[0]*2, self.pos[1] + delta[1]*2)
            if self.get_board().onBoard(pos):
                self.try_to_move_to(pos)
                break
            direction.next()
        self.breed_cooldown_down()

    def collision(self, attacker) -> bool:
        if random.random() < self.ESCAPE_CHANCE:
            direction = self.world.get_direction()()
            direction.randomise()

            for i in range(direction.directions()):
                delta = direction.delta()
                pos = (self.pos[0] + delta[0] * 2, self.pos[1] + delta[1] * 2)
                if self.get_board().onBoard(pos):
                    self.try_to_move_to(pos)
                    break
                direction.next()
            print("Antylopa", self.pos, "ucieka od", attacker.get_name(), attacker.get_pos())
            return True
        else:
            return super(Antelope, self).collision(attacker)
