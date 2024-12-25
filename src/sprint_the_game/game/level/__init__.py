import pyxel

from typing import Tuple, Union
from sprint_the_game import gui
from sprint_the_game.event import GameEvent
from sprint_the_game.game import Conf
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
        i = 0 if self.conf.selected_level is None else self.conf.selected_level
        i, j = i % 5, i // 5

        LEVEL_X, LEVEL_Y = i * 24, j * 12

        pyxel.bltm(0, 0, 0, pyxel.width, 0, pyxel.width, pyxel.height)

        pyxel.rectb(
            (256 - 8 * 24) // 2 - 1, (144 - 8 * 12) // 2 - 1, 24 * 8 + 2, 8 * 12 + 2, 7
        )
        pyxel.rect((256 - 8 * 24) // 2, (144 - 8 * 12) // 2, 24 * 8, 8 * 12, 0)

        pyxel.bltm(
            (256 - 8 * 24) // 2,
            (144 - 8 * 12) // 2,
            1,
            8 * LEVEL_X,
            8 * LEVEL_Y,
            8 * 24,
            8 * 12,
        )

        text = "Sprint - Level " + str(self.conf.selected_level)
        x, y = (256 - 4 * len(text)) // 2, 13

        gui.text_box(x, y, text)

        self.gui.draw()
