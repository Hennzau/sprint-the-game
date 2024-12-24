import pyxel

from typing import Tuple
from sprint_the_game import gui
from sprint_the_game.event import GameEvent
from sprint_the_game.game import Conf
from sprint_the_game.gui.static import StaticGUI
from sprint_the_game.state import GameState


class LevelSelectorConf(Conf):
    pass


class LevelSelector:
    def __init__(self, conf: LevelSelectorConf):
        self.gui = StaticGUI()

        self.events: list[GameEvent] = []

        self.gui.add(
            3, "Back", lambda: self.events.append(GameEvent.LEVEL_SELECTOR_TO_MAIN_MENU)
        )

        for i in range (3):
            for j in range (5):
                self.gui.add(
                    i, "Level " + str(i * 3 + j + 1) , lambda: self.events.append(GameEvent.LEVEL_SELECTOR_TO_MAIN_MENU)
                )

    def update_conf(self, conf: Conf | None):
        pass

    def update(self) -> Tuple[GameState, Conf | None]:
        self.gui.update()

        while len(self.events) > 0:
            event = self.events.pop()

            if event == GameEvent.LEVEL_SELECTOR_TO_MAIN_MENU:
                return (GameState.MAIN_MENU, None)

        return (GameState.LEVEL_SELECTOR, None)

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height)

        text = "Sprint - Level Selector"
        x, y = (256 - 4 * len(text)) // 2, 16

        gui.text_box(x, y, text)

        self.gui.draw()
