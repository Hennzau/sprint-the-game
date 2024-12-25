from enum import Enum


class Tile(Enum):
    EMPTY = (0, 0)

    BLUE = (0, 1)
    YELLOW = (2, 0)
    PINK = (3, 0)

    WALL = (3, 1)
