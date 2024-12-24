import pyxel

from typing import Tuple
from sprint_the_game import gui
from sprint_the_game.event import GameEvent
from sprint_the_game.game import Conf
from sprint_the_game.gui.static import StaticGUI
from sprint_the_game.state import GameState
from dataclasses import dataclass


@dataclass
class LevelConf(Conf):
    selected_level: int | None


class Level:
    def __init__(self, conf: LevelConf):
        self.gui = StaticGUI()

        self.events: list[GameEvent] = []

        self.selected_level = None

        self.gui.add(
            3, "Back", lambda: self.events.append(GameEvent.LEVEL_TO_LEVEL_SELECTOR)
        )

    def level_event(self, level: int):
        self.selected_level = level
        self.events.append(GameEvent.LEVEL_SELECTOR_TO_LEVEL)

    def update_conf(self, conf: Conf | None):
        if not isinstance(conf, LevelConf):
            return

        self.selected_level = conf.selected_level

    def update(self) -> Tuple[GameState, Conf | None]:
        self.gui.update()

        while len(self.events) > 0:
            event = self.events.pop()

            if event == GameEvent.LEVEL_TO_LEVEL_SELECTOR:
                return (GameState.LEVEL_SELECTOR, None)

        return (GameState.LEVEL, None)

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height)

        text = "Sprint - Level " + str(self.selected_level)
        x, y = (256 - 4 * len(text)) // 2, 16

        gui.text_box(x, y, text)

        self.gui.draw()
