from enum import Enum


class GameState(Enum):
    QUIT = 0
    MAIN_MENU = 1
    OPTIONS = 2
    LEVEL_EDITOR = 3
    LEVEL_SELECTOR = 4
