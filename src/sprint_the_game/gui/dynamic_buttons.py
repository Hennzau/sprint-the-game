from typing import Tuple, Union
from typing import Callable

import pyxel
import time

from sprint_the_game import gui


class DynamicButtons:
    def __init__(self):
        self.buttons: dict[int, Tuple[Tuple[int, int], Tuple[str, Callable]]] = {}
        self.progress: dict[int, Tuple[float, float]] = {}

    def add(self, key: int, x: int, y: int, str: str, callback: Callable) -> None:
        self.buttons[key] = ((x, y), (str, callback))
        self.progress[key] = (0.0, 0.0)

    def update(self):
        for key in self.buttons:
            if pyxel.btnr(key):
                self.progress[key] = (0.0, 0.0)

            if pyxel.btn(key):
                if self.progress[key] == (0.0, 0.0):
                    self.progress[key] = (time.time(), 0.0)
                else:
                    progress = time.time() - self.progress[key][0]  # type: ignore
                    if progress >= 0.5:
                        self.progress[key] = (0.0, 0.0)

                        (x, y), (str, callable) = self.buttons[key]

                        callable()

                    else:
                        self.progress[key] = (self.progress[key][0], progress)  # type: ignore

    def draw(self):
        for key in self.buttons:
            (x, y), (str, callable) = self.buttons[key]
            length = (self.progress[key][1] / 0.5) * len(str) * 4

            color = 9 if length <= 0.0 else 7
            pyxel.text(x, y, str, color, None)

            pyxel.rect(x, y + 8, length, 2, 7)
