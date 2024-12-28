import pyxel

from typing import Tuple, Union
from sprint_the_game import gui
from sprint_the_game.event import GameEvent
from sprint_the_game.game.conf import Conf
from sprint_the_game.game.level_editor import LevelEditorConf
from sprint_the_game.gui.static_buttons import StaticButtons
from sprint_the_game.state import GameState
from dataclasses import dataclass


@dataclass
class LevelEditorLevelSelectorConf(Conf):
    pass


class LevelEditorLevelSelector:
    def __init__(self, conf: LevelEditorLevelSelectorConf):
        self.gui = StaticButtons()

        self.events: list[Tuple[GameEvent, GameState, Union[Conf, None]]] = []

        self.gui.add(
            3,
            "Back",
            lambda: self.events.append(
                (GameEvent.CHANGE_STATE, GameState.MAIN_MENU, None)
            ),
        )

        for i in range(3):
            for j in range(5):
                level = i * 5 + j + 1

                self.gui.add(
                    i,
                    "Level " + str(level),
                    lambda level=level: self.events.append(
                        (
                            GameEvent.CHANGE_STATE,
                            GameState.LEVEL_EDITOR,
                            LevelEditorConf(selected_level=level),
                        )
                    ),
                )

    def update_conf(self, conf: Conf | None):
        pass

    def update(self) -> Tuple[GameState, Conf | None]:
        self.gui.update()

        while len(self.events) > 0:
            (event, state, conf) = self.events.pop()

            if event == GameEvent.CHANGE_STATE:
                return (state, conf)

        return (GameState.LEVEL_EDITOR_LEVEL_SELECTOR, None)

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height)

        text = "Sprint - Editor Selector"
        x, y = (256 - 4 * len(text)) // 2, 14

        gui.text_box(x, y, text)

        self.gui.draw()
