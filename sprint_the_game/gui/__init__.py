import pyxel


def text_box(x: int, y: int, text: str):
    size = len(text)

    pyxel.rect(x - 3, y - 3, 4 * size + 6, 12, 7)
    pyxel.rect(x - 2, y - 2, 4 * size + 4, 10, 5)
    pyxel.text(x, y, text, 9, None)
