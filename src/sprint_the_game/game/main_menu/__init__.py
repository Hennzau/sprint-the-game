import pyxel

from typing import Tuple
from sprint_the_game import gui
from sprint_the_game.event import GameEvent
from sprint_the_game.game import Conf, level_selector
from sprint_the_game.gui.static import StaticGUI
from sprint_the_game.state import GameState


class MainMenuConf(Conf):
    pass


class MainMenu:
    def __init__(self, conf: MainMenuConf):
        self.gui = StaticGUI()

        self.events: list[GameEvent] = []

        self.gui.add(
            0, "Start", lambda: self.events.append(GameEvent.MAIN_MENU_TO_LEVEL_SELECTOR)
        )
        self.gui.add(
            0, "Editor", lambda: self.events.append(GameEvent.MAIN_MENU_TO_LEVEL_EDITOR)
        )
        self.gui.add(
            1, "Options", lambda: self.events.append(GameEvent.MAIN_MENU_TO_OPTIONS)
        )
        self.gui.add(
            2, "Quit", lambda: self.events.append(GameEvent.MAIN_MENU_TO_QUIT)
        )

    def update_conf(self, conf: Conf | None):
        pass

    def update(self) -> Tuple[GameState, Conf | None]:
        self.gui.update()

        while len(self.events) > 0:
            event = self.events.pop()

            if event == GameEvent.MAIN_MENU_TO_QUIT:
                return (GameState.QUIT, None)

            if event == GameEvent.MAIN_MENU_TO_OPTIONS:
                return (GameState.OPTIONS, None)

            if event == GameEvent.MAIN_MENU_TO_LEVEL_EDITOR:
                return (GameState.LEVEL_EDITOR, None)

            if event == GameEvent.MAIN_MENU_TO_LEVEL_SELECTOR:
                return (GameState.LEVEL_SELECTOR, None)

        return (GameState.MAIN_MENU, None)

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height)

        text = "Sprint - The Game"
        x, y = (256 - 4 * len(text)) // 2, 16

        gui.text_box(x, y, text)

        self.gui.draw()
