from InterfaceElement import InterfaceElement


class GridContainer(InterfaceElement):

    def __init__(self, pos: (int, int), size: (int, int), dimensions: (int, int)):
        self.pos = pos
        self.fieldSize = (size[0] // dimensions[0], size[1] // dimensions[1])
        self.dimensions = dimensions
        self.size = size
        self.grid = [[None for i in range(dimensions[0])] for j in range(dimensions[1])]

    def draw(self, surface):
        for row in self.grid:
            for field in row:
                field.draw(surface)

    def moveTo(self, pos: (int, int)):
        self.pos = pos

    def collides(self, point):
        return self.pos[0] <= point[0] <= self.pos[0] + self.size[0] \
               and self.pos[1] <= point[1] <= self.pos[1] + self.size[1]

    def handle_event(self, event):
        # if self.collides(event.pos):
        for row in self.grid:
            for field in row:
                field.handle_event(event)

    def update(self):
        for row in self.grid:
            for field in row:
                field.update()

    def in_bounds(self, pos: (int, int)):
        return 0 <= pos[0] < self.dimensions[0] and 0 <= pos[1] <= self.dimensions[1]

    def set_element(self, element, pos: (int, int)):
        if self.in_bounds(pos):
            self.grid[pos[0]][pos[1]] = element
