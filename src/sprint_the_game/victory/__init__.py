from sprint_the_game.state import GameState


class Victory:
    def __init__(self):
        pass

    def update(self) -> GameState:
        return GameState.VICTORY

    def draw(self):
        pass
