from typing import Tuple
from sprint_the_game.event import GameEvent
from sprint_the_game.game.conf import Conf
from sprint_the_game.game.level import Level, LevelConf
from sprint_the_game.state import GameState


def update_conf(level: Level, conf: Conf | None):
    if not isinstance(conf, LevelConf):
        return

    level.conf = conf


def update(level: Level) -> Tuple[GameState, Conf | None]:
    level.gui.update()

    while len(level.events) > 0:
        (event, state, conf) = level.events.pop()

        if event == GameEvent.CHANGE_STATE:
            return (state, conf)

    return (GameState.LEVEL, None)
