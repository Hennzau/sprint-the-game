import pyxel

from typing import Tuple, Union
from sprint_the_game import gui
from sprint_the_game.event import GameEvent
from sprint_the_game.game import Conf
from sprint_the_game.game.level.tile import Tile
from sprint_the_game.game.level_editor import LevelEditorConf
from sprint_the_game.gui.static_buttons import StaticButtons
from sprint_the_game.state import GameState


class MainMenuConf(Conf):
    pass


class MainMenu:
    def __init__(self, conf: MainMenuConf):
        self.gui = StaticButtons()

        self.events: list[Tuple[GameEvent, GameState, Union[Conf, None]]] = []

        self.gui.add(
            0,
            "Start",
            lambda: self.events.append(
                (GameEvent.CHANGE_STATE, GameState.LEVEL_SELECTOR, None)
            ),
        )
        self.gui.add(
            0,
            "Editor",
            lambda: self.events.append(
                (
                    GameEvent.CHANGE_STATE,
                    GameState.LEVEL_EDITOR,
                    LevelEditorConf(selected_tile=Tile.WALL, selected_level=None),
                )
            ),
        )
        self.gui.add(
            1,
            "Options",
            lambda: self.events.append(
                (GameEvent.CHANGE_STATE, GameState.OPTIONS, None)
            ),
        )
        self.gui.add(
            2,
            "Quit",
            lambda: self.events.append((GameEvent.CHANGE_STATE, GameState.QUIT, None)),
        )

    def update_conf(self, conf: Conf | None):
        pass

    def update(self) -> Tuple[GameState, Conf | None]:
        self.gui.update()

        while len(self.events) > 0:
            (event, state, conf) = self.events.pop()

            if event == GameEvent.CHANGE_STATE:
                return (state, conf)

        return (GameState.MAIN_MENU, None)

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height)

        text = "Sprint - The Game"
        x, y = (256 - 4 * len(text)) // 2, 14

        gui.text_box(x, y, text)

        self.gui.draw()
