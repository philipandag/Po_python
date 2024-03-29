from Organisms.Animals.Animal import Animal


class Fox(Animal):
    NAME = "Fox"
    SYMBOL = "F"
    COLOR = (255, 134, 0)
    STRENGTH = 3
    INITIATIVE = 7

    def __init__(self):
        super(Fox, self).__init__(Fox.NAME, Fox.SYMBOL, Fox.COLOR, Fox.STRENGTH, Fox.INITIATIVE)

    def action(self):
        direction = self.world.get_direction()()
        direction.randomise()

        for i in range(direction.directions()):
            delta = direction.delta()
            pos = (self.pos[0] + delta[0], self.pos[1] + delta[1])
            if self.get_board().onBoard(pos):
                if not self.get_board().at(pos).is_empty():
                    if self.get_board().at(pos).get_organism().get_strength() <= self.get_strength():
                        self.try_to_move_to(pos)
                        break
                else:
                    self.try_to_move_to(pos)
                    break
            direction.next()
