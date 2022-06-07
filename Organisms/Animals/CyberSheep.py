from Organisms.Animals.Animal import Animal
from Organisms.Animals.Sheep import Sheep
from Organisms.Plants.PineBorscht import PineBorscht
from numpy import sign


class CyberSheep(Animal):
    NAME = "CyberSheep"
    SYMBOL = "#"
    ATTACK_COLOR = (0, 0, 255)
    COLOR = (150, 150, 220)
    STRENGTH = 11
    INITIATIVE = 4
    def __init__(self):
        super(CyberSheep, self).__init__(CyberSheep.NAME, CyberSheep.SYMBOL, CyberSheep.COLOR, CyberSheep.STRENGTH, CyberSheep.INITIATIVE)

    def action(self):
        dir = self.search_for_pine()
        if dir is not None:
            self.try_to_move_to((self.pos[0] + dir[0], self.pos[1] + dir[1]))
            self.breed_cooldown_down()
        else:
            super(CyberSheep, self).action()

    def search_for_pine(self):
        shortest_distance = self.get_board().dimensions[0] * self.get_board().dimensions[1]
        closest = None

        for y in range(self.get_board().dimensions[1]):
            for x in range(self.get_board().dimensions[0]):
                if isinstance(self.get_board().at((x,y)).get_organism(), PineBorscht):
                    distance = abs(self.pos[0] - x) + abs(self.pos[1] - y)
                    if distance < shortest_distance:
                        shortest_distance = distance
                        closest = (x, y)
        if closest is not None:
            self.color = self.ATTACK_COLOR
            delta = (closest[0] - self.pos[0], closest[1] - self.pos[1])
            dir = (sign(delta[0]), sign(delta[1]))
            return dir
        self.color = self.COLOR
        return None



