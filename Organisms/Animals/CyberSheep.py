from Organisms.Animals.Animal import Animal


class CyberSheep(Animal):
    NAME = "CyberSheep"
    SYMBOL = "#"
    COLOR = (29, 0, 255)
    STRENGTH = 11
    INITIATIVE = 4
    def __init__(self):
        super(CyberSheep, self).__init__(CyberSheep.NAME, CyberSheep.SYMBOL, CyberSheep.COLOR, CyberSheep.STRENGTH, CyberSheep.INITIATIVE)