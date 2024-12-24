from typing import Tuple
from sprint_the_game.game import Conf
from sprint_the_game.state import GameState


class MainMenuConf(Conf):
    pass


class MainMenu:
    def __init__(self, conf: MainMenuConf):
        pass

    def update_conf(self, conf: Conf | None):
        pass

    def update(self) -> Tuple[GameState, Conf | None]:
        return (GameState.MAIN_MENU, None)

    def draw(self):
        pass
