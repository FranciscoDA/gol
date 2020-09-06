import argparse

import pygame as pg

from .game import Game
from .drawing_thread import DrawingThread
from .themes import DefaultTheme, GridTheme, HeatmapTheme, HeatmapGridTheme


THEMES = {
    'default': DefaultTheme,
    'grid': GridTheme,
    'heatmap': HeatmapTheme,
    'heatmapgrid': HeatmapGridTheme,
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rows', type=int, default=12, help='Number of rows in the board')
    parser.add_argument('--cols', type=int, default=16, help='Number of columns in the board')
    parser.add_argument('--theme', type=str, choices=THEMES.keys(), default=None, help='Theme')
    parser.add_argument('--resx', type=int, default=800, help='Vertical resolution')
    parser.add_argument('--resy', type=int, default=600, help='Horizontal resolution')
    args = parser.parse_args()

    pg.init()

    board_rows = args.rows
    board_columns = args.cols

    theme = None
    if args.theme:
        theme = THEMES[args.theme]()

    screen_width = args.resx
    screen_height = args.resy

    game = Game(board_rows, board_columns, screen_width, screen_height)

    drawing_thread = DrawingThread(game, theme)
    drawing_thread.init_screen(screen_width, screen_height)
    drawing_thread.start()

    try:
        game.main_loop()
    finally:
        drawing_thread.quit()

if __name__ == '__main__':
    main()
