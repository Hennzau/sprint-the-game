import pyxel
import argparse

from sprint_the_game.game.level import Level, LevelConf
from sprint_the_game.game.level_editor import LevelEditor, LevelEditorConf
from sprint_the_game.game.level_editor_level_selector import (
    LevelEditorLevelSelector,
    LevelEditorLevelSelectorConf,
)
from sprint_the_game.game.level_selector import LevelSelector, LevelSelectorConf
from sprint_the_game.game.main_menu import MainMenu, MainMenuConf
from sprint_the_game.game.options import Options, OptionsConf
from sprint_the_game.state import GameState

resource_path = None


class App:
    def __init__(self):
        pyxel.init(256, 144, title="Sprint The Game", display_scale=5)

        parser = argparse.ArgumentParser(
            prog="Sprint The Game",
            description="Play to the game",
        )

        parser.add_argument("filepath")
        args = parser.parse_args()

        global resource_path
        resource_path = f"{args.filepath}/my_resource.pyxres"
        pyxel.load(resource_path)

        self.state = {
            GameState.MAIN_MENU: MainMenu(MainMenuConf()),
            GameState.OPTIONS: Options(OptionsConf()),
            GameState.LEVEL_EDITOR: LevelEditor(LevelEditorConf()),
            GameState.LEVEL_SELECTOR: LevelSelector(LevelSelectorConf()),
            GameState.LEVEL: Level(LevelConf()),
            GameState.LEVEL_EDITOR_LEVEL_SELECTOR: LevelEditorLevelSelector(
                LevelEditorLevelSelectorConf()
            ),
        }

        self.current_state = GameState.MAIN_MENU

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        (next_state, conf) = self.state[self.current_state].update()

        if next_state == GameState.QUIT:
            pyxel.quit()
            return

        if self.current_state != next_state:
            pyxel.mouse(False)

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
