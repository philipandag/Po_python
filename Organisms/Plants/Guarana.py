from Organisms.Plants.Plant import Plant


class Guarana(Plant):
    NAME = "Guarana"
    SYMBOL = "G"
    COLOR = (180, 80, 50)
    STRENGTH = 1
    def __init__(self):
        super(Guarana, self).__init__(Guarana.NAME, Guarana.SYMBOL, Guarana.COLOR, Guarana.STRENGTH)
