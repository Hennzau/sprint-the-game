from enum import Enum


class GameEvent(Enum):
    MAIN_MENU_TO_PLAYING = (1,)
    MAIN_MENU_TO_LEAVE = (2,)
    MAIN_MENU_TO_OPTIONS = (3,)
