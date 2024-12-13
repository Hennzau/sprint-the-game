import pyxel
from sprint_the_game.state import GameState


class MainMenu:
    def __init__(self):
        pass

    def update(self) -> GameState:
        if pyxel.btn(pyxel.KEY_RETURN):
            return GameState.PLAYING

        return GameState.MAIN_MENU

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height)

        pyxel.text(pyxel.width // 2 - 48, pyxel.height // 2, "Press Enter to start", 1, None)
