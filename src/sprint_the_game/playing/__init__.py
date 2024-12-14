import pyxel
from sprint_the_game.state import GameState


class Playing:
    def __init__(self):
        pass

    def update(self) -> GameState:
        if pyxel.btn(pyxel.KEY_BACKSPACE):
            return GameState.MAIN_MENU

        return GameState.PLAYING

    def draw(self):
        pyxel.text(
            pyxel.width // 2 - 48, pyxel.height // 2, "You're now playing", 1, None
        )
