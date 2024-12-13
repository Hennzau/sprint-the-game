import pyxel

from sprint_the_game.level_editor import LeveLEditor
from sprint_the_game.main_menu import MainMenu
from sprint_the_game.playing import Playing
from sprint_the_game.state import GameState
from sprint_the_game.victory import Victory


class App:
    def __init__(self):
        pyxel.init(256, 144, title="Sprint The Game", display_scale=5)

        self.state = GameState.MAIN_MENU

        pyxel.load("../../my_resource.pyxres")

        self.game = {
            GameState.MAIN_MENU: MainMenu(),
            GameState.LEVEL_EDITOR: LeveLEditor(),
            GameState.PLAYING: Playing(),
            GameState.VICTORY: Victory(),
        }

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        next_state = self.game[self.state].update()

        self.state = next_state

    def draw(self):
        pyxel.cls(0)

        self.game[self.state].draw()


def main() -> None:
    app = App()
    app.run()


if __name__ == "__main__":
    main()
