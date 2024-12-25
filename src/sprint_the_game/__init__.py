import pyxel

from sprint_the_game.game.level import Level, LevelConf
from sprint_the_game.game.level_editor import LevelEditor, LevelEditorConf
from sprint_the_game.game.level_selector import LevelSelector, LevelSelectorConf
from sprint_the_game.game.main_menu import MainMenu, MainMenuConf
from sprint_the_game.game.options import Options, OptionsConf
from sprint_the_game.state import GameState


class App:
    def __init__(self):
        pyxel.init(256, 144, title="Sprint The Game", display_scale=5)

        pyxel.load("../../my_resource.pyxres")

        self.state = {
            GameState.MAIN_MENU: MainMenu(MainMenuConf()),
            GameState.OPTIONS: Options(OptionsConf(main_theme=True, sounds=True)),
            GameState.LEVEL_EDITOR: LevelEditor(LevelEditorConf()),
            GameState.LEVEL_SELECTOR: LevelSelector(LevelSelectorConf()),
            GameState.LEVEL: Level(LevelConf(None)),
        }

        self.current_state = GameState.MAIN_MENU

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        (next_state, conf) = self.state[self.current_state].update()

        if next_state == GameState.QUIT:
            pyxel.quit()
            return

        self.state[next_state].update_conf(conf)
        self.current_state = next_state

    def draw(self):
        pyxel.cls(0)

        self.state[self.current_state].draw()


def main() -> None:
    app = App()
    app.run()


if __name__ == "__main__":
    main()
