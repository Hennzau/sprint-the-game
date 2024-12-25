import pyxel

from typing import Tuple, Union
from sprint_the_game import gui
from sprint_the_game.event import GameEvent
from sprint_the_game.game import Conf
from sprint_the_game.game.level.tile import Tile
from sprint_the_game.game.level_editor import LevelEditorConf
from sprint_the_game.gui.dynamic_buttons import DynamicButtons
from sprint_the_game.gui.static_buttons import StaticButtons
from sprint_the_game.state import GameState
from dataclasses import dataclass


@dataclass
class LevelConf(Conf):
    selected_level: int | None


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
                    LevelEditorConf(selected_level=self.conf.selected_level, selected_tile=Tile.WALL),
                )
            ),
        )

    def update_conf(self, conf: Conf | None):
        if not isinstance(conf, LevelConf):
            return

        self.conf = conf

    def update(self) -> Tuple[GameState, Conf | None]:
        self.gui.update()

        while len(self.events) > 0:
            (event, state, conf) = self.events.pop()

            if event == GameEvent.CHANGE_STATE:
                return (state, conf)

        return (GameState.LEVEL, None)

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height)

        text = "Sprint - Level " + str(self.conf.selected_level)
        x, y = (256 - 4 * len(text)) // 2, 14

        gui.text_box(x, y, text)

        self.gui.draw()
