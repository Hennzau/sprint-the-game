from typing import Tuple
from typing import Callable

import pyxel


class StaticButtons:
    def __init__(self):
        self.buttons: list[list[Tuple[str, Callable]]] = [[], [], [], [], []]
        self.button = None

    def add(self, line: int, str: str, callback: Callable) -> None:
        if line >= 5:
            return

        self.buttons[line].append((str, callback))

    def modify_text(self, line: int, i: int, str: str):
        self.buttons[line][i] = (str, self.buttons[line][i][1])

    def max_vertical_level(self) -> int:
        if not len(self.buttons[4]) == 0:
            return 5
        elif not len(self.buttons[3]) == 0:
            return 4
        elif not len(self.buttons[2]) == 0:
            return 3
        elif not len(self.buttons[1]) == 0:
            return 2
        elif not len(self.buttons[0]) == 0:
            return 1

        return 0

    def min_vertical_level(self) -> int:
        if not len(self.buttons[0]) == 0:
            return 1
        elif not len(self.buttons[1]) == 0:
            return 2
        elif not len(self.buttons[2]) == 0:
            return 3
        elif not len(self.buttons[3]) == 0:
            return 4
        elif not len(self.buttons[4]) == 0:
            return 5

        return 6

    def update(self):
        if self.max_vertical_level() == 0:
            return

        if self.button is None:
            v = self.min_vertical_level() - 1
            self.button = (0, v)

        if pyxel.btnp(pyxel.KEY_LEFT):
            self.button = (max(0, self.button[0] - 1), self.button[1])

        if pyxel.btnp(pyxel.KEY_RIGHT):
            v = len(self.buttons[self.button[1]])

            self.button = (min(self.button[0] + 1, v - 1), self.button[1])

        if pyxel.btnp(pyxel.KEY_UP):
            if len(self.buttons[max(self.button[1] - 1, 0)]) >= self.button[0] + 1:
                self.button = (self.button[0], max(self.button[1] - 1, 0))
            else:
                self.button = (
                    len(self.buttons[max(self.button[1] - 1, 0)]) - 1,
                    max(self.button[1] - 1, 0),
                )

        if pyxel.btnp(pyxel.KEY_DOWN):
            v = self.max_vertical_level()

            if len(self.buttons[min(self.button[1] + 1, v - 1)]) >= self.button[0] + 1:
                self.button = (self.button[0], min(self.button[1] + 1, v - 1))
            else:
                self.button = (
                    len(self.buttons[min(self.button[1] + 1, v - 1)]) - 1,
                    min(self.button[1] + 1, v - 1),
                )

        if pyxel.btnp(pyxel.KEY_RETURN):
            if 0 <= self.button[1] < len(self.buttons):
                if 0 <= self.button[0] < len(self.buttons[self.button[1]]):
                    self.buttons[self.button[1]][self.button[0]][1]()

    def draw(self):
        if self.max_vertical_level() == 0:
            return

        max_horizontal = max(
            len(self.buttons[1]),
            len(self.buttons[0]),
            len(self.buttons[2]),
            len(self.buttons[3]),
            len(self.buttons[4]),
        )
        max_vertical = self.max_vertical_level()

        size_w = (256 - 64) // max(2, max_horizontal)
        size_h = (144 - 64) // max(3, max_vertical)

        y = (144 - size_h * max_vertical) // 2

        for j in range(len(self.buttons)):
            for i, (str, _) in enumerate(self.buttons[j]):
                gap_x = 1
                gap_y = 1

                x = (256 - size_w * len(self.buttons[j])) // 2

                pyxel.rect(
                    x + size_w * i + gap_x,
                    y + size_h * j + gap_y,
                    size_w - gap_x * 2,
                    size_h - gap_y * 2,
                    1,
                )

        for j in range(len(self.buttons)):
            for i, (str, _) in enumerate(self.buttons[j]):
                x = (256 - size_w * len(self.buttons[j])) // 2

                s_t = len(str) * 4

                tx = x + (size_w - s_t) // 2
                ty = y + (size_h - 6) // 2

                color = (
                    9
                    if self.button is None
                    else 7
                    if (self.button[0] == i and self.button[1] == j)
                    else 9
                )

                if self.button is not None and (
                    self.button[0] == i and self.button[1] == j
                ):
                    pyxel.rect(
                        tx + size_w * i - 2,
                        ty + size_h * j - 2,
                        s_t + 4,
                        6 + 4,
                        7,
                    )
                    pyxel.rect(
                        tx + size_w * i - 1,
                        ty + size_h * j - 1,
                        s_t + 2,
                        6 + 2,
                        1,
                    )

                pyxel.text(tx + size_w * i, ty + size_h * j, str, color, None)
