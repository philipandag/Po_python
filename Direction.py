from abc import ABCMeta

from enum import EnumMeta


class Direction(ABCMeta, EnumMeta):

    def __init__(self):
        self.value: Direction = Direction.N

    def randomise(self) -> None:
        pass

    def next(self) -> None:
        pass

    def delta(self) -> (int, int):
        pass

    def directions(self) -> int:
        pass
