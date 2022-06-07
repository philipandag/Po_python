from Organisms.Animals.Animal import Animal
from Organisms.Plants.Plant import Plant


class PineBorscht(Plant):
    NAME = "PineBorscht"
    SYMBOL = "P"
    COLOR = (255, 255, 0)
    STRENGTH = 1
    def __init__(self):
        super(PineBorscht, self).__init__(PineBorscht.NAME, PineBorscht.SYMBOL, PineBorscht.COLOR, PineBorscht.STRENGTH)

    def action(self):
        direction = self.world.get_direction()()
        for i in range(direction.directions()):
            delta = direction.delta()
            pos = (self.pos[0] + delta[0], self.pos[1] + delta[1])
            if self.get_board().onBoard(pos) \
                    and not self.get_board().at(pos).is_empty() \
                    and isinstance(self.get_board().at(pos).get_organism(), Animal)\
                    and not self.get_board().at(pos).get_organism().get_name() == "CyberSheep":
                self.get_board().at(pos).get_organism().kill()
            direction.next()
        super(PineBorscht, self).action()
