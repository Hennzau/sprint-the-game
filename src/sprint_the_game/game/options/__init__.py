import pyxel

from typing import Tuple, Union
from sprint_the_game import gui
from sprint_the_game.event import GameEvent
from sprint_the_game.game import Conf
from sprint_the_game.gui.static_buttons import StaticButtons
from sprint_the_game.state import GameState


class OptionsConf(Conf):
    pass


class Options:
    def __init__(self, conf: OptionsConf):
        self.gui = StaticButtons()

        self.events: list[Tuple[GameEvent, GameState, Union[Conf, None]]] = []

        self.gui.add(
            0, "Back", lambda: self.events.append((GameEvent.CHANGE_STATE, GameState.MAIN_MENU,None))
        )
        self.gui.add(
            1, "Back", lambda: self.events.append((GameEvent.CHANGE_STATE, GameState.MAIN_MENU,None))
        )
        self.gui.add(
            2, "Back", lambda: self.events.append((GameEvent.CHANGE_STATE, GameState.MAIN_MENU,None))
        )
        self.gui.add(
            3, "Back", lambda: self.events.append((GameEvent.CHANGE_STATE, GameState.MAIN_MENU,None))
        )
        self.gui.add(
            4, "Back", lambda: self.events.append((GameEvent.CHANGE_STATE, GameState.MAIN_MENU,None))
        )

    def update_conf(self, conf: Conf | None):
        pass

    def update(self) -> Tuple[GameState, Conf | None]:
        self.gui.update()

        while len(self.events) > 0:
            (event, state, conf) = self.events.pop()

            if event == GameEvent.CHANGE_STATE:
                return (state, conf)

        return (GameState.OPTIONS, None)

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height)

        text = "Sprint - Options"
        x, y = (256 - 4 * len(text)) // 2, 16

        gui.text_box(x, y, text)

        self.gui.draw()
