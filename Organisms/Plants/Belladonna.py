from Organisms.Plants.Plant import Plant


class Belladonna(Plant):
    NAME = "Belladonna"
    SYMBOL = "B"
    COLOR = (255, 0, 10)
    STRENGTH = 99
    def __init__(self):
        super(Belladonna, self).__init__(Belladonna.NAME, Belladonna.SYMBOL, Belladonna.COLOR, Belladonna.STRENGTH)

    def collision(self, attacker) -> bool:
        super(Belladonna, self).collision(attacker)
        attacker.kill()