import os

import pygame as pg
pg.font.init()

FONTS_DIR = os.path.join("resources", "fonts")

COMPUTER_FONT = os.path.join(FONTS_DIR, "Computerfont.ttf")
FONT_SIZE = 28
FONT_COLOR = pg.color.THECOLORS['white']
FONT_BACKGROUND = pg.color.THECOLORS['black']

font = pg.font.Font(COMPUTER_FONT, FONT_SIZE)


def get_text(text_string):
    text = font.render(text_string, False, FONT_COLOR, FONT_BACKGROUND)
    return text
