import pyxel

from typing import List
from sprint_the_game.game.level.cube import Cube
from sprint_the_game.game.level.tile import Tile


class Cubes:
    def __init__(self):
        self.end_points = {}

        self.cubes: List[Cube] = []

    def load_level(self, level: int):
        i, j = level % 5, level // 5

        LEVEL_X, LEVEL_Y = i * 24, j * 12

        self.cubes: List[Cube] = []
        self.end_points = {}

        for i in range(24):
            for j in range(12):
                tile = Tile(pyxel.tilemaps[1].pget(i + LEVEL_X, j + LEVEL_Y))

                if (
                    tile == Tile.YELLOW_START
                    or tile == Tile.PINK_START
                    or tile == Tile.GREEN_START
                    or tile == Tile.BLUE_START
                ):
                    self.cubes.append(Cube((i, j), tile, level))

                if (
                    tile == Tile.YELLOW_END
                    or tile == Tile.PINK_END
                    or tile == Tile.GREEN_END
                    or tile == Tile.BLUE_END
                ):
                    self.end_points[(i, j)] = tile

    def is_moving(self) -> bool:
        return any(cube.is_moving() for cube in self.cubes)

    def update(self):
        for cube in self.cubes:
            cube.update()

        if not self.is_moving():
            if pyxel.btnp(pyxel.KEY_RIGHT):
                for cube in self.cubes:
                    cube.move_right()

            if pyxel.btnp(pyxel.KEY_LEFT):
                for cube in self.cubes:
                    cube.move_left()

            if pyxel.btnp(pyxel.KEY_UP):
                for cube in self.cubes:
                    cube.move_up()

            if pyxel.btnp(pyxel.KEY_DOWN):
                for cube in self.cubes:
                    cube.move_down()

    def draw(self):
        for cube in self.cubes:
            cube.draw()
