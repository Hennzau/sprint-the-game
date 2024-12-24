import pyxel

from typing import Tuple, Union
from sprint_the_game import gui
from sprint_the_game.event import GameEvent
from sprint_the_game.game import Conf
from sprint_the_game.game.level import LevelConf
from sprint_the_game.gui.static import StaticGUI
from sprint_the_game.state import GameState


class LevelSelectorConf(Conf):
    pass


class LevelSelector:
    def __init__(self, conf: LevelSelectorConf):
        self.gui = StaticGUI()

        self.events: list[Tuple[GameEvent, Union[int, None]]] = []

        self.gui.add(
            3,
            "Back",
            lambda: self.events.append((GameEvent.LEVEL_SELECTOR_TO_MAIN_MENU, None)),
        )

        for i in range(3):
            for j in range(5):
                level = i * 5 + j + 1

                self.gui.add(
                    i,
                    "Level " + str(level),
                    lambda level=level: self.events.append(
                        (GameEvent.LEVEL_SELECTOR_TO_LEVEL, level)
                    ),
                )

    def update_conf(self, conf: Conf | None):
        pass

    def update(self) -> Tuple[GameState, Conf | None]:
        self.gui.update()

        while len(self.events) > 0:
            (event, level) = self.events.pop()

            if event == GameEvent.LEVEL_SELECTOR_TO_MAIN_MENU:
                return (GameState.MAIN_MENU, None)

            if event == GameEvent.LEVEL_SELECTOR_TO_LEVEL:
                return (GameState.LEVEL, LevelConf(level))

        return (GameState.LEVEL_SELECTOR, None)

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height)

        text = "Sprint - Level Selector"
        x, y = (256 - 4 * len(text)) // 2, 16

        gui.text_box(x, y, text)

        self.gui.draw()
