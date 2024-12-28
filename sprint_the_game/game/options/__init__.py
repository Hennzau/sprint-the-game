import pyxel

from dataclasses import dataclass

from typing import Tuple, Union
from sprint_the_game import gui
from sprint_the_game.event import GameEvent
from sprint_the_game.game.conf import Conf
from sprint_the_game.gui.static_buttons import StaticButtons
from sprint_the_game.state import GameState


@dataclass
class OptionsConf(Conf):
    main_theme: bool = True
    sounds: bool = True
    lights: bool = True
    particles: bool = True


class Options:
    def __init__(self, conf: OptionsConf):
        self.gui = StaticButtons()
        self.conf = conf

        self.events: list[Tuple[GameEvent, GameState, Union[Conf, None]]] = []

        self.gui.add(
            0,
            "Disable Main Theme",
            lambda: self.events.append(
                (
                    GameEvent.CHANGE_CONF,
                    GameState.OPTIONS,
                    OptionsConf(
                        main_theme=not self.conf.main_theme,
                        sounds=self.conf.sounds,
                        lights=self.conf.lights,
                        particles=self.conf.particles,
                    ),
                )
            ),
        )
        self.gui.add(
            1,
            "Disable Sounds",
            lambda: self.events.append(
                (
                    GameEvent.CHANGE_CONF,
                    GameState.OPTIONS,
                    OptionsConf(
                        main_theme=self.conf.main_theme,
                        sounds=not self.conf.sounds,
                        lights=self.conf.lights,
                        particles=self.conf.particles,
                    ),
                )
            ),
        )
        self.gui.add(
            2,
            "Disable Lights",
            lambda: self.events.append(
                (
                    GameEvent.CHANGE_CONF,
                    GameState.OPTIONS,
                    OptionsConf(
                        main_theme=self.conf.main_theme,
                        sounds=self.conf.sounds,
                        lights=not self.conf.lights,
                        particles=self.conf.particles,
                    ),
                )
            ),
        )
        self.gui.add(
            3,
            "Disable Particles",
            lambda: self.events.append(
                (
                    GameEvent.CHANGE_CONF,
                    GameState.OPTIONS,
                    OptionsConf(
                        main_theme=self.conf.main_theme,
                        sounds=self.conf.sounds,
                        lights=self.conf.lights,
                        particles=not self.conf.particles,
                    ),
                )
            ),
        )
        self.gui.add(
            4,
            "Back",
            lambda: self.events.append(
                (GameEvent.CHANGE_STATE, GameState.MAIN_MENU, None)
            ),
        )

    def update_conf(self, conf: Conf | None):
        if isinstance(conf, OptionsConf):
            self.conf = conf

            self.gui.modify_text(
                0,
                0,
                "Enable Main Theme"
                if not self.conf.main_theme
                else "Disable Main Theme",
            )
            self.gui.modify_text(
                1, 0, "Enable Sounds" if not self.conf.sounds else "Disable Sounds"
            )
            self.gui.modify_text(
                2, 0, "Enable Lights" if not self.conf.lights else "Disable Lights"
            )
            self.gui.modify_text(
                3,
                0,
                "Enable Particles" if not self.conf.particles else "Disable Particles",
            )

    def update(self) -> Tuple[GameState, Conf | None]:
        self.gui.update()

        while len(self.events) > 0:
            (event, state, conf) = self.events.pop()

            if event == GameEvent.CHANGE_STATE:
                return (state, conf)
            elif event == GameEvent.CHANGE_CONF:
                return (GameState.OPTIONS, conf)

        return (GameState.OPTIONS, None)

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height)

        text = "Sprint - Options"
        x, y = (256 - 4 * len(text)) // 2, 14

        gui.text_box(x, y, text)

        self.gui.draw()
