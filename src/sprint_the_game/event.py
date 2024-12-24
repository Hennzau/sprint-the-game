from enum import Enum


class GameEvent(Enum):
    MAIN_MENU_TO_LEVEL_SELECTOR = 0
    MAIN_MENU_TO_QUIT = 1
    MAIN_MENU_TO_OPTIONS = 2
    MAIN_MENU_TO_LEVEL_EDITOR = 5

    OPTIONS_TO_MAIN_MENU = 3

    LEVEL_EDITOR_TO_MAIN_MENU = 4

    LEVEL_SELECTOR_TO_MAIN_MENU = 6
    LEVEL_SELECTOR_TO_LEVEL = 7

    LEVEL_TO_MAIN_MENU = 8
