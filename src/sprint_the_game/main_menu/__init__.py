import pyxel
from sprint_the_game.gui import StaticGUI
from sprint_the_game.event import GameEvent
from sprint_the_game.state import GameState


class MainMenu:
    def __init__(self):
        self.gui = StaticGUI()

        self.events: list[GameEvent] = []

        self.gui.add(
            0, "Start", lambda: self.events.append(GameEvent.MAIN_MENU_TO_PLAYING)
        )
        self.gui.add(
            0, "Quit", lambda: self.events.append(GameEvent.MAIN_MENU_TO_LEAVE)
        )
        self.gui.add(
            1, "Options", lambda: self.events.append(GameEvent.MAIN_MENU_TO_OPTIONS)
        )

    def update(self) -> GameState:
        self.gui.update()

        while len(self.events) > 0:
            event = self.events.pop()

            if event == GameEvent.MAIN_MENU_TO_LEAVE:
                return GameState.LEAVING

            if event == GameEvent.MAIN_MENU_TO_PLAYING:
                return GameState.PLAYING

        return GameState.MAIN_MENU

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height)

        pyxel.rect((256 - 4 * 17) // 2 - 3, 32 - 3, 4 * 17 + 6, 12, 7)
        pyxel.rect((256 - 4 * 17) // 2 - 2, 32 - 2, 4 * 17 + 4, 10, 5)
        pyxel.text((256 - 4 * 17) // 2, 32, "Sprint - The Game", 9, None)

        self.gui.draw()
