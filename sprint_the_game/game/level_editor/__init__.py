import pyxel

from typing import Tuple, Union
from sprint_the_game.event import GameEvent
from sprint_the_game.game.conf import Conf
from sprint_the_game.game.level.cubes import Cubes
from sprint_the_game.game.level.tile import Tile
from sprint_the_game.gui.dynamic_buttons import DynamicButtons
from sprint_the_game.state import GameState
from dataclasses import dataclass


@dataclass
class LevelEditorConf(Conf):
    selected_level: int | None = None
    selected_tile: Tile = Tile.WALL


class LevelEditor:
    def __init__(self, conf: LevelEditorConf):
        self.gui = DynamicButtons()

        self.events: list[Tuple[GameEvent, GameState, Union[Conf, None]]] = []
        self.conf = conf

        self.gui.add(
            pyxel.KEY_Q,
            12,
            132,
            "Hold q to go back",
            lambda: self.events.append(
                (GameEvent.CHANGE_STATE, GameState.LEVEL_EDITOR_LEVEL_SELECTOR, None)
            ),
        )

        self.gui.add(
            pyxel.KEY_SPACE,
            92,
            132,
            "Hold space to save",
            lambda: self.events.append(
                (GameEvent.SAVE_LEVEL, GameState.LEVEL_EDITOR, None)
            ),
        )

        self.gui.add(
            pyxel.KEY_R,
            180,
            132,
            "Hold r to reload",
            lambda: self.events.append(
                (GameEvent.RELOAD_LEVEL, GameState.LEVEL_EDITOR, None)
            ),
        )

        self.cubes = Cubes()

    def update_conf(self, conf: Conf | None):
        from sprint_the_game.game.level_editor.update import update_conf

        update_conf(self, conf)

    def update(self) -> Tuple[GameState, Conf | None]:
        from sprint_the_game.game.level_editor.update import update

        return update(self)

    def draw(self):
        from sprint_the_game.game.level_editor.draw import draw

        draw(self)
