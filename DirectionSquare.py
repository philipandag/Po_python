import random

from Direction import Direction


class DirectionSquare(Direction):
    N = 0
    NE = 1
    E = 2
    SE = 3
    S = 4
    SW = 5
    W = 6
    NW = 7
    DIRECTIONS = 8
    def __init__(self):
        super(DirectionSquare, self).__init__()

    def randomise(self):
        self.value = random(list(DirectionSquare))

    def next(self):
        if self.value == DirectionSquare.NW:
            self.value = DirectionSquare.N
        else:
            self.value = self.value + 1

    def delta(self) -> (int, int):
        dx, dy = 0, 0
        if DirectionSquare.N < self.value < DirectionSquare.S:
            dx = 1
        elif DirectionSquare.S < self.value <= DirectionSquare.NE:
            dx = -1
        if self.value > DirectionSquare.W or self.value < DirectionSquare.E:
            dy = -1
        elif DirectionSquare.W > self.value > DirectionSquare.E:
            dy = 1
        return dx, dy

    def directions(self) -> int:
        return self.DIRECTIONS
