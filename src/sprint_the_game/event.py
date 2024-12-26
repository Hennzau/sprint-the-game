from enum import Enum


class GameEvent(Enum):
    CHANGE_STATE = 0
    CHANGE_CONF = 1
    RELOAD_LEVEL = 2
    SAVE_LEVEL = 3
    ERASE_LEVEL = 4
