from typing import Type

from OrganismChooserButton import OrganismChooserButton

from GridContainer import GridContainer
from Organisms.Animals.Human import Human
from Organisms.Plants.Belladonna import Belladonna
from Organisms.Plants.Dandelion import Dandelion
from Organisms.Plants.Grass import Grass
from Organisms.Organism import Organism
from Organisms.Plants.Guarana import Guarana
from Organisms.Plants.PineBorscht import PineBorscht


class OrganismChooser(GridContainer):

    animals: Type[Organism] = [Human]
    plants: Type[Organism] = [Grass, Dandelion, Guarana, Belladonna, PineBorscht]

    def __init__(self, pos: (int, int), size: (int, int)):
        super(OrganismChooser, self).__init__(pos, size, (7, 2))
        self.choosenOrganism: Type[Organism]
        self.createButtons()
        self.world = None

    def createButtons(self):
        self.grid = [[], []]
        for i in range(len(self.animals)):
            self.grid[0].append(OrganismChooserButton(self.fieldSize, (self.pos[0] + self.fieldSize[0] * i, self.pos[1]), self.animals[i]))
        for i in range(len(self.plants)):
            self.grid[0].append(OrganismChooserButton(self.fieldSize, (self.pos[0] + self.fieldSize[0] * i, self.pos[1] + self.size[1]/2), self.plants[i]))

    def setWorld(self, world):
        self.world = world
        for row in self.grid:
            for f in row:
                f.set_world(world)
