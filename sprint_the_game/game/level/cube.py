import pyxel
import numpy as np

from enum import Enum
from typing import Tuple, Union
from sprint_the_game.game.level.tile import Tile


class CubeTile(Enum):
    YELLOW = (2, 6)
    PINK = (2, 7)
    GREEN = (4, 6)
    BLUE = (4, 7)


class Cube:
    def __init__(self, starting_pos: Tuple[int, int], initial_tile: Tile, level: int):
        if not (0 <= starting_pos[0] < 24) or not (0 <= starting_pos[1] < 12):
            raise ValueError("position must be contained in the grid")

        if not (
            initial_tile == Tile.YELLOW_START
            or initial_tile == Tile.PINK_START
            or initial_tile == Tile.GREEN_START
            or initial_tile == Tile.BLUE_START
        ):
            raise ValueError("tile must be YELLOW, PINK, GREEN or BLUE start")

        self.pos = starting_pos
        self.initial_tile = initial_tile
        self.current_tile = (
            CubeTile.YELLOW
            if initial_tile == Tile.YELLOW_START
            else CubeTile.PINK
            if initial_tile == Tile.PINK_START
            else CubeTile.GREEN
            if initial_tile == Tile.GREEN_START
            else CubeTile.BLUE
        )
        self.render_pos = np.array(self.pos, dtype=np.float32) * 8
        self.render_tile = self.current_tile
        self.level = level

        self.end = False

    def update(self):
        self.render_pos = np.array(self.pos, dtype=np.float32) * 8
        self.render_tile = self.current_tile

        i, j = self.level % 5, self.level // 5

        LEVEL_X, LEVEL_Y = i * 24, j * 12

        tile = Tile(
            pyxel.tilemaps[1].pget(self.pos[0] + LEVEL_X, self.pos[1] + LEVEL_Y)
        )

        if self.initial_tile == Tile.BLUE_START and tile == Tile.BLUE_END:
            self.end = True
        elif self.initial_tile == Tile.GREEN_START and tile == Tile.GREEN_END:
            self.end = True
        elif self.initial_tile == Tile.PINK_START and tile == Tile.PINK_END:
            self.end = True
        elif self.initial_tile == Tile.YELLOW_START and tile == Tile.YELLOW_END:
            self.end = True
        else:
            self.end = False

    def draw(self):
        u, v = self.render_tile.value

        pyxel.blt(
            (256 - 8 * 24) // 2 + int(self.render_pos[0]),
            (144 - 8 * 12) // 2 + int(self.render_pos[1]),
            0,
            u * 8,
            v * 8,
            8,
            8,
            0,
        )

        u, v = self.initial_tile.value

        pyxel.blt(
            (256 - 8 * 24) // 2 + int(self.render_pos[0]),
            (144 - 8 * 12) // 2 + int(self.render_pos[1]),
            0,
            u * 8,
            v * 8,
            8,
            8,
            0,
        )

    def is_start(self, tile: Tile) -> bool:
        return tile in [
            Tile.BLUE_START,
            Tile.PINK_START,
            Tile.YELLOW_START,
            Tile.GREEN_START,
        ]

    def is_end(self, tile: Tile) -> bool:
        return tile in [Tile.BLUE_END, Tile.PINK_END, Tile.YELLOW_END, Tile.GREEN_END]

    def is_switch(self, tile: Tile) -> bool:
        return tile in [
            Tile.BLUE_SWITCH,
            Tile.PINK_SWITCH,
            Tile.YELLOW_SWITCH,
            Tile.GREEN_SWITCH,
        ]

    def is_wall(self, tile: Tile) -> bool:
        return tile in [Tile.BLUE, Tile.PINK, Tile.YELLOW, Tile.GREEN]

    def corresponding_cube(self, tile: Tile) -> Union[CubeTile, None]:
        return (
            CubeTile.YELLOW
            if tile == Tile.YELLOW
            else CubeTile.PINK
            if tile == Tile.PINK
            else CubeTile.GREEN
            if tile == Tile.GREEN
            else CubeTile.BLUE
            if tile == Tile.BLUE
            else None
        )

    def handle_tile(self, active_tile: CubeTile, tile: Tile) -> Tuple[bool, CubeTile]:
        if tile == Tile.EMPTY or self.is_start(tile) or self.is_end(tile):
            return (True, active_tile)

        if self.is_switch(tile):
            return (
                True,
                CubeTile.YELLOW
                if tile == Tile.YELLOW_SWITCH
                else CubeTile.PINK
                if tile == Tile.PINK_SWITCH
                else CubeTile.GREEN
                if tile == Tile.GREEN_SWITCH
                else CubeTile.BLUE,
            )

        if self.is_wall(tile):
            if active_tile == self.corresponding_cube(tile):
                return (True, active_tile)

        return (tile == Tile.EMPTY, active_tile)

    def move(self, inc_x: int, inc_y: int) -> Tuple[int, int, CubeTile]:
        i, j = self.level % 5, self.level // 5

        LEVEL_X, LEVEL_Y = i * 24, j * 12

        x, y = self.pos

        active_tile = self.current_tile

        if inc_x != 0:
            while 0 <= x < 24:
                if x + inc_x < 0 or x + inc_x >= 24:
                    break

                tile = Tile(pyxel.tilemaps[1].pget(x + inc_x + LEVEL_X, y + LEVEL_Y))

                move, active_tile = self.handle_tile(active_tile, tile)

                if not move:
                    break

                x += inc_x

        if inc_y != 0:
            while 0 <= y < 12:
                if y + inc_y < 0 or y + inc_y >= 12:
                    break

                tile = Tile(pyxel.tilemaps[1].pget(x + LEVEL_X, y + inc_y + LEVEL_Y))

                move, active_tile = self.handle_tile(active_tile, tile)

                if not move:
                    break

                y += inc_y

        return (x, y, active_tile)

    def move_right(self):
        (x, y, tile) = self.move(1, 0)
        self.pos = (x, y)
        self.current_tile = tile

    def move_left(self):
        (x, y, tile) = self.move(-1, 0)
        self.pos = (x, y)
        self.current_tile = tile

    def move_up(self):
        (x, y, tile) = self.move(0, -1)
        self.pos = (x, y)
        self.current_tile = tile

    def move_down(self):
        (x, y, tile) = self.move(0, 1)
        self.pos = (x, y)
        self.current_tile = tile

    def is_moving(self) -> bool:
        x = self.pos[0] * 8
        y = self.pos[1] * 8

        xx = int(self.render_pos[0])
        yy = int(self.render_pos[1])

        return x != xx or y != yy
