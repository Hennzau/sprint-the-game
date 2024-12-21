import pyxel


class App:
    def __init__(self):
        pyxel.init(256, 144, title="Sprint The Game", display_scale=5)

        pyxel.load("../../my_resource.pyxres")

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)


def main() -> None:
    app = App()
    app.run()


if __name__ == "__main__":
    main()
