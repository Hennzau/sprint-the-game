from sprint_the_game.state import GameState


class Playing:
    def __init__(self):
        pass

    def update(self) -> GameState:
        return GameState.PLAYING

    def draw(self):
        pass
