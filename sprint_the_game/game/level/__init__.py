import pyxel

from typing import Tuple, Union
from sprint_the_game.event import GameEvent
from sprint_the_game.game.conf import Conf
from sprint_the_game.game.level.cubes import Cubes
from sprint_the_game.game.level_editor import LevelEditorConf
from sprint_the_game.gui.dynamic_buttons import DynamicButtons
from sprint_the_game.state import GameState
from dataclasses import dataclass


@dataclass
class LevelConf(Conf):
    selected_level: int | None = None


class Level:
    def __init__(self, conf: LevelConf):
        self.gui = DynamicButtons()

        self.events: list[Tuple[GameEvent, GameState, Union[Conf, None]]] = []

        self.conf = conf

        self.gui.add(
            pyxel.KEY_Q,
            12,
            123,
            "Hold q to go back",
            lambda: self.events.append(
                (GameEvent.CHANGE_STATE, GameState.LEVEL_SELECTOR, None)
            ),
        )

        self.gui.add(
            pyxel.KEY_R,
            98,
            123,
            "Hold r to reload",
            lambda: self.events.append(
                (GameEvent.RELOAD_LEVEL, GameState.LEVEL_SELECTOR, None)
            ),
        )

        self.gui.add(
            pyxel.KEY_E,
            188,
            123,
            "Hold e to edit",
            lambda: self.events.append(
                (
                    GameEvent.CHANGE_STATE,
                    GameState.LEVEL_EDITOR,
                    LevelEditorConf(selected_level=self.conf.selected_level),
                )
            ),
        )

        self.cubes = Cubes()
        self.end: float | None = None

    def update_conf(self, conf: Conf | None):
        from sprint_the_game.game.level.update import update_conf

        update_conf(self, conf)

    def update(self) -> Tuple[GameState, Conf | None]:
        from sprint_the_game.game.level.update import update

        return update(self)

    def draw(self):
        from sprint_the_game.game.level.draw import draw

        draw(self)
