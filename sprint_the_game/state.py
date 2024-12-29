from enum import Enum


class GameState(Enum):
    QUIT = 0
    MAIN_MENU = 1
    OPTIONS = 2
    LEVEL_EDITOR = 3
    LEVEL_SELECTOR = 4
    LEVEL = 5
    LEVEL_EDITOR_LEVEL_SELECTOR = 6

    GO_BACK = 7

    VICTORY = 8
