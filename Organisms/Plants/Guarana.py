from Organisms.Plants.Plant import Plant


class Guarana(Plant):
    NAME = "Guarana"
    SYMBOL = "G"
    COLOR = (180, 80, 50)
    STRENGTH = 1
    STRENGTH_BONUS = 3
    def __init__(self):
        super(Guarana, self).__init__(Guarana.NAME, Guarana.SYMBOL, Guarana.COLOR, Guarana.STRENGTH)

    def collision(self, attacker) -> bool:
        attacker.delta_strength(self.STRENGTH_BONUS)
        return super(Guarana, self).collision(attacker)
