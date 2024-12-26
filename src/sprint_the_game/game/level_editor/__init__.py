import pyxel

from typing import Tuple, Union
from sprint_the_game import gui
import sprint_the_game
from sprint_the_game.event import GameEvent
from sprint_the_game.game import Conf
from sprint_the_game.game.level.tile import Tile
from sprint_the_game.gui.dynamic_buttons import DynamicButtons
from sprint_the_game.state import GameState
from dataclasses import dataclass


@dataclass
class LevelEditorConf(Conf):
    selected_level: int | None = None
    selected_tile: Tile = Tile.WALL
    erase: bool = False
    overwrite: bool = False


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
                (GameEvent.CHANGE_STATE, GameState.MAIN_MENU, None)
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
            pyxel.KEY_E,
            180,
            132,
            "Hold e to select",
            lambda: self.events.append(
                (GameEvent.CHANGE_STATE, GameState.LEVEL_EDITOR_LEVEL_SELECTOR, None)
            ),
        )

    def update_conf(self, conf: Conf | None):
        pyxel.mouse(True)

        if isinstance(conf, LevelEditorConf):
            can_overwrite = (
                self.conf.selected_level is None and conf.selected_level is not None
            )

            self.conf = conf

            i = 0 if self.conf.selected_level is None else self.conf.selected_level
            i, j = i % 5, i // 5

            LEVEL_X, LEVEL_Y = i * 24, j * 12

            if self.conf.erase:
                u, v = Tile.EMPTY.value

                for i in range(24):
                    for j in range(12):
                        pyxel.tilemaps[1].set(
                            i,
                            j,
                            [f"0{u}0{v} "],
                        )

            elif (
                self.conf.overwrite and can_overwrite
            ):  # copy the editor into this level
                for i in range(24):
                    for j in range(12):
                        u, v = pyxel.tilemaps[1].pget(i, j)
                        pyxel.tilemaps[1].set(
                            LEVEL_X + i,
                            LEVEL_Y + j,
                            [f"0{u}0{v} "],
                        )

    def update(self) -> Tuple[GameState, Conf | None]:
        i = 0 if self.conf.selected_level is None else self.conf.selected_level
        i, j = i % 5, i // 5

        LEVEL_X, LEVEL_Y = i * 24, j * 12

        self.gui.update()

        while len(self.events) > 0:
            (event, state, conf) = self.events.pop()

            if event == GameEvent.CHANGE_STATE:
                return (state, conf)
            elif event == GameEvent.SAVE_LEVEL:
                pyxel.save(sprint_the_game.resource_path)

        x, y = pyxel.mouse_x // 8, pyxel.mouse_y // 8

        if 4 <= x < 28 and 3 <= y < 15:
            x = x - 4
            y = y - 3

            u, v = (
                self.conf.selected_tile.value
                if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT)
                else Tile.EMPTY.value
            )

            if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) or pyxel.btn(
                pyxel.MOUSE_BUTTON_LEFT
            ):
                pyxel.tilemaps[1].set(
                    x + LEVEL_X,
                    y + LEVEL_Y,
                    [f"0{u}0{v}"],
                )

        if pyxel.btnv(pyxel.MOUSE_WHEEL_Y):
            tiles = [tile for tile in Tile]
            cursor = tiles.index(self.conf.selected_tile)

            cursor = max(0, min(len(tiles) - 2, cursor - pyxel.mouse_wheel))
            self.conf.selected_tile = tiles[cursor]

        return (GameState.LEVEL_EDITOR, None)

    def draw(self):
        i = 0 if self.conf.selected_level is None else self.conf.selected_level
        i, j = i % 5, i // 5

        LEVEL_X, LEVEL_Y = i * 24, j * 12

        pyxel.bltm(0, 0, 0, pyxel.width * 2, 0, pyxel.width, pyxel.height)

        pyxel.rectb(
            (256 - 8 * 24) // 2 - 1, (144 - 8 * 12) // 2 - 1, 24 * 8 + 2, 8 * 12 + 2, 7
        )
        pyxel.rect((256 - 8 * 24) // 2, (144 - 8 * 12) // 2, 24 * 8, 8 * 12, 1)

        pyxel.bltm(
            (256 - 8 * 24) // 2,
            (144 - 8 * 12) // 2,
            1,
            8 * LEVEL_X,
            8 * LEVEL_Y,
            8 * 24,
            8 * 12,
            0
        )

        text = (
            "Sprint - Editor (?)"
            if self.conf.selected_level is None
            else f"Sprint - Editor ({self.conf.selected_level})"
        )
        x, y = (256 - 4 * len(text)) // 2, 13

        gui.text_box(x, y, text)
        self.gui.draw()

        x, y = pyxel.mouse_x // 8, pyxel.mouse_y // 8

        if 4 <= x < 28 and 3 <= y < 15:
            u, v = self.conf.selected_tile.value
            pyxel.blt(x * 8, y * 8, 0, u * 8, v * 8, 8, 8, 0)

        tiles = [tile for tile in Tile]
        cursor = tiles.index(self.conf.selected_tile)

        for i in range(len(tiles) - 1):
            u, v = tiles[i].value

            y, x = i % 6, i // 6
            pyxel.blt(4 + x * 16 + x//2 * 199, 24 + y * 16, 0, u * 8, v * 8, 8, 8, 0)

        y, x = cursor % 6, cursor // 6
        pyxel.rectb(4 + x * 16 + x//2 * 199 - 1, 24 + y * 16 - 1, 10, 10, 7)
