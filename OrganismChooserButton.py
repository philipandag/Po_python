from Button import Button
from typing import Type
from Organisms.Organism import Organism

class OrganismChooserButton(Button):
    def __init__(self, size, position, organism_class: Type[Organism]):
        super(OrganismChooserButton, self).__init__(size, position)
        organism = organism_class()
        self.organism_class = organism_class
        self.set_color(organism.get_colour())
        self.setText(organism.get_name())
        self.world = None

    def set_world(self, world):
        self.world = world

    def onClick(self):
        self.world.set_chosen_organism(self.organism_class)

