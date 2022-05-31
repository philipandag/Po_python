from Organisms.Plants.Plant import Plant


class Belladonna(Plant):
    NAME = "Belladonna"
    SYMBOL = "B"
    COLOR = (255, 0, 10)
    STRENGTH = 1
    def __init__(self):
        super(Belladonna, self).__init__(Belladonna.NAME, Belladonna.SYMBOL, Belladonna.COLOR, Belladonna.STRENGTH)
