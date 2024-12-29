import pyxel

from dataclasses import dataclass

from typing import Tuple, Union
from sprint_the_game import gui
from sprint_the_game.event import GameEvent
from sprint_the_game.game.conf import Conf
from sprint_the_game.game.level import LevelConf
from sprint_the_game.gui.static_buttons import StaticButtons
from sprint_the_game.state import GameState


@dataclass
class VictoryConf(Conf):
    current_level: int | None = None


class Victory:
    def __init__(self, conf: VictoryConf):
        self.gui = StaticButtons()
        self.conf = conf

        self.events: list[Tuple[GameEvent, GameState, Union[Conf, None]]] = []

        self.gui.add(
            0,
            "Retry",
            lambda: self.events.append(
                (
                    GameEvent.CHANGE_STATE,
                    GameState.LEVEL,
                    LevelConf(selected_level=self.conf.current_level),
                )
            ),
        )
        self.gui.add(
            0,
            "Next",
            lambda: self.events.append(
                (
                    GameEvent.CHANGE_STATE,
                    GameState.LEVEL,
                    LevelConf(
                        selected_level=min(self.conf.current_level + 1, 15)
                        if self.conf.current_level is not None
                        else None
                    ),
                )
            ),
        )
        self.gui.add(
            1,
            "Back",
            lambda: self.events.append(
                (GameEvent.CHANGE_STATE, GameState.LEVEL_SELECTOR, None)
            ),
        )

    def update_conf(self, conf: Conf | None):
        if isinstance(conf, VictoryConf):
            self.conf = conf

    def update(self) -> Tuple[GameState, Conf | None]:
        self.gui.update()

        while len(self.events) > 0:
            (event, state, conf) = self.events.pop()

            if event == GameEvent.CHANGE_STATE:
                return (state, conf)

        return (GameState.VICTORY, None)

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height)

        text = "Sprint - Victory"
        x, y = (256 - 4 * len(text)) // 2, 14

        gui.text_box(x, y, text)

        self.gui.draw()
