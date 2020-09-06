from threading import Thread, Condition

import pygame as pg
from pygame.locals import DOUBLEBUF, OPENGL

from .themes import DefaultTheme


class DrawingThread(Thread):
    def __init__(self, game, theme=None, target_fps=60):
        super().__init__()
        self.game = game
        self.last_cycle_count = -1
        self.target_fps = 60
        self.exit_condition = Condition()
        self.screen = None
        if theme is None:
            self.theme = DefaultTheme()
        else:
            self.theme = theme

    def init_screen(self, screen_width, screen_height):
        screen_size = (screen_width, screen_height)
        screen_flags = DOUBLEBUF
        color_depth = pg.display.mode_ok(screen_size, screen_flags, 32)
        self.screen = pg.display.set_mode(screen_size, screen_flags, color_depth)

    def run(self):
        with self.exit_condition:
            while not self.exit_condition.wait(1 / self.target_fps):
                if self.catch_up():
                    self.theme.draw_board(self.screen, self.game.board)
                    pg.display.flip()

    def is_dirty(self):
        return self.last_cycle_count != self.game.cycles

    def catch_up(self):
        result = self.is_dirty()
        self.last_cycle_count = self.game.cycles
        return result

    def quit(self):
        with self.exit_condition:
            self.exit_condition.notify_all()

