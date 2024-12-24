import pyxel

from typing import Tuple
from sprint_the_game import gui
from sprint_the_game.event import GameEvent
from sprint_the_game.game import Conf
from sprint_the_game.gui.static import StaticGUI
from sprint_the_game.state import GameState


class LevelEditorConf(Conf):
    pass


class LevelEditor:
    def __init__(self, conf: LevelEditorConf):
        self.gui = StaticGUI()

        self.events: list[GameEvent] = []

        self.gui.add(
            0, "Back", lambda: self.events.append(GameEvent.LEVEL_EDITOR_TO_MAIN_MENU)
        )

    def update_conf(self, conf: Conf | None):
        pass

    def update(self) -> Tuple[GameState, Conf | None]:
        self.gui.update()

        while len(self.events) > 0:
            event = self.events.pop()

            if event == GameEvent.LEVEL_EDITOR_TO_MAIN_MENU:
                return (GameState.MAIN_MENU, None)

        return (GameState.LEVEL_EDITOR, None)

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height)

        text = "Sprint - Editor"
        x, y = (256 - 4 * len(text)) // 2, 16

        gui.text_box(x, y, text)

        self.gui.draw()
