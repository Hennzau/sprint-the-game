from enum import Enum


class Tile(Enum):
    YELLOW = (2, 4)
    PINK = (2, 5)
    GREEN = (4, 4)
    BLUE = (4, 5)

    YELLOW_SWITCH = (3, 4)
    PINK_SWITCH = (3, 5)
    GREEN_SWITCH = (5, 4)
    BLUE_SWITCH = (5, 5)

    YELLOW_START = (0, 6)
    PINK_START = (0, 7)
    GREEN_START = (1, 6)
    BLUE_START = (1, 7)

    YELLOW_END = (3, 6)
    PINK_END = (3, 7)
    GREEN_END = (5, 6)
    BLUE_END = (5, 7)

    WALL = (1, 4)

    EMPTY = (0, 4)
