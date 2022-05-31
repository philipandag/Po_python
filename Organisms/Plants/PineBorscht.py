from Organisms.Plants.Plant import Plant


class PineBorscht(Plant):
    NAME = "PineBorscht"
    SYMBOL = "P"
    COLOR = (255, 255, 0)
    STRENGTH = 1
    def __init__(self):
        super(PineBorscht, self).__init__(PineBorscht.NAME, PineBorscht.SYMBOL, PineBorscht.COLOR, PineBorscht.STRENGTH)
