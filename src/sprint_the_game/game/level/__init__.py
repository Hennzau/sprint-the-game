import pyxel

from typing import Tuple, Union
from sprint_the_game import gui
from sprint_the_game.event import GameEvent
from sprint_the_game.game import Conf
from sprint_the_game.gui.static_buttons import StaticButtons
from sprint_the_game.state import GameState
from dataclasses import dataclass


@dataclass
class LevelConf(Conf):
    selected_level: int | None


class Level:
    def __init__(self, conf: LevelConf):
        self.gui = StaticButtons()

        self.events: list[Tuple[GameEvent, GameState, Union[Conf, None]]] = []

        self.selected_level = None

        self.gui.add(
            3,
            "Back",
            lambda: self.events.append(
                (GameEvent.CHANGE_STATE, GameState.LEVEL_SELECTOR, None)
            ),
        )

    def update_conf(self, conf: Conf | None):
        if not isinstance(conf, LevelConf):
            return

        self.selected_level = conf.selected_level

    def update(self) -> Tuple[GameState, Conf | None]:
        self.gui.update()

        while len(self.events) > 0:
            (event, state, conf) = self.events.pop()

            if event == GameEvent.CHANGE_STATE:
                return (state, conf)

        return (GameState.LEVEL, None)

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height)

        text = "Sprint - Level " + str(self.selected_level)
        x, y = (256 - 4 * len(text)) // 2, 16

        gui.text_box(x, y, text)

        self.gui.draw()
