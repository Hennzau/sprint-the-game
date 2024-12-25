import pyxel

from typing import Tuple, Union
from sprint_the_game import gui
from sprint_the_game.event import GameEvent
from sprint_the_game.game import Conf
from sprint_the_game.game.level.tile import Tile
from sprint_the_game.gui.dynamic_buttons import DynamicButtons
from sprint_the_game.gui.static_buttons import StaticButtons
from sprint_the_game.state import GameState
from dataclasses import dataclass


@dataclass
class LevelEditorConf(Conf):
    selected_level: int | None
    selected_tile: Tile


class LevelEditor:
    def __init__(self, conf: LevelEditorConf):
        self.gui = DynamicButtons()

        self.events: list[Tuple[GameEvent, GameState, Union[Conf, None]]] = []
        self.conf = conf

        self.gui.add(
            pyxel.KEY_Q,
            12,
            123,
            "Hold q to go back",
            lambda: self.events.append(
                (GameEvent.CHANGE_STATE, GameState.MAIN_MENU, None)
            ),
        )

        self.gui.add(
            pyxel.KEY_SPACE,
            92,
            123,
            "Hold space to save",
            lambda: self.events.append(
                (GameEvent.SAVE_LEVEL, GameState.LEVEL_EDITOR, None)
            ),
        )

        self.gui.add(
            pyxel.KEY_E,
            180,
            123,
            "Hold e to select",
            lambda: self.events.append(
                (GameEvent.CHANGE_STATE, GameState.LEVEL_EDITOR_LEVEL_SELECTOR, None)
            ),
        )

        pyxel.mouse(True)

    def update_conf(self, conf: Conf | None):
        pyxel.mouse(True)

        if isinstance(conf, LevelEditorConf):
            self.conf = conf

    def update(self) -> Tuple[GameState, Conf | None]:
        self.gui.update()

        while len(self.events) > 0:
            (event, state, conf) = self.events.pop()

            if event == GameEvent.CHANGE_STATE:
                return (state, conf)
            elif event == GameEvent.SAVE_LEVEL:
                pyxel.save("../../my_resource.pyxres")

        x, y = pyxel.mouse_x // 8, pyxel.mouse_y // 8

        if 4 <= x < 28 and 3 <= y < 15:
            x = x - 4
            y = y - 3

            u, v = self.conf.selected_tile.value if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) else Tile.EMPTY.value

            if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) or pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                pyxel.tilemaps[1].set(
                    x,
                    y,
                    [
                        f"0{u}0{v}"
                    ],
                )

        if pyxel.btnv(pyxel.MOUSE_WHEEL_Y):
            tiles = [tile for tile in Tile]
            cursor = tiles.index(self.conf.selected_tile)

            cursor = max(1, min(len(tiles) - 1, cursor - pyxel.mouse_wheel))
            self.conf.selected_tile = tiles[cursor]

            print(cursor)


        return (GameState.LEVEL_EDITOR, None)

    def draw(self):
        pyxel.bltm(0, 0, 0, pyxel.width, 0, pyxel.width, pyxel.height)

        pyxel.rectb((256 - 8 * 24) // 2 - 1, (144 - 8 * 12) // 2 - 1, 24 * 8 + 2, 8 * 12 + 2, 7)
        pyxel.rect((256 - 8 * 24) // 2, (144 - 8 * 12) // 2, 24 * 8, 8 * 12, 0)

        pyxel.bltm((256 - 8 * 24) // 2, (144 - 8 * 12) // 2, 1, 0, 0, 8 * 24, 8 * 12)

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
            pyxel.blt(x * 8, y * 8, 0, u * 8, v * 8, 8, 8)

        tiles = [tile for tile in Tile]
        cursor = tiles.index(self.conf.selected_tile)

        for i in range(1, len(tiles)):
            u, v = tiles[i].value

            pyxel.blt(16, i * 16, 0, u * 8, v * 8, 8, 8)

        pyxel.rectb(16 - 1, - 1 + cursor * 16, 10, 10, 7)
