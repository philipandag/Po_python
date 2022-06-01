import enum
from abc import ABCMeta
from abc import ABC

from enum import EnumMeta
from enum import Enum

#class DirectionMeta(ABCMeta, EnumMeta):
 #   pass

class Direction(ABC):

    def randomise(self) -> None:
        pass

    def next(self) -> None:
        pass

    def delta(self) -> (int, int):
        pass

    def directions(self) -> int:
        pass
