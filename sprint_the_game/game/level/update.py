import time

from typing import Tuple
from sprint_the_game.event import GameEvent
from sprint_the_game.game.conf import Conf
from sprint_the_game.game.level import Level, LevelConf
from sprint_the_game.game.victory import VictoryConf
from sprint_the_game.state import GameState


def update_conf(level: Level, conf: Conf | None):
    if not isinstance(conf, LevelConf):
        return

    level.conf = conf
    if level.conf.selected_level is not None:
        level.cubes.load_level(level.conf.selected_level)


def update(level: Level) -> Tuple[GameState, Conf | None]:
    level.gui.update()

    while len(level.events) > 0:
        (event, state, conf) = level.events.pop()

        if event == GameEvent.CHANGE_STATE:
            return (state, conf)
        elif event == GameEvent.RELOAD_LEVEL:
            if level.conf.selected_level is not None:
                level.cubes.load_level(level.conf.selected_level)

    if level.end is None:
        level.cubes.update()

        if not level.cubes.is_moving():
            end = {}
            for cube in level.cubes.cubes:
                if cube.end:
                    if cube.pos not in end:
                        end[cube.pos] = None

            if len(end) == len(level.cubes.cubes):
                level.end = time.time()
    else:
        if time.time() - level.end > 0.5:
            level.end = None
            return (
                GameState.VICTORY,
                VictoryConf(current_level=level.conf.selected_level),
            )

    return (GameState.LEVEL, None)
