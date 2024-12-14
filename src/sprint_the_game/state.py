from enum import Enum


class GameState(Enum):
    MAIN_MENU = (1,)
    LEVEL_EDITOR = (2,)
    PLAYING = (3,)
    VICTORY = (4,)
    LEAVING = (5,)
    OPTIONS = (6,)
