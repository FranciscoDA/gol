import pygame as pg

from .board import Board
from . import patterns


class Game:
    PAUSE_THRESHOLD = 3

    def __init__(self, board_rows, board_cols, screen_width, screen_height):
        self.board = Board.from_zeros(board_rows, board_cols)

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.cycles = 0
        self.framerate = self.PAUSE_THRESHOLD
        self.clock = pg.time.Clock()
        self.quit = False

    def update(self):
        self.board.update()

    def main_loop(self):
        while not self.quit:
            if self.framerate > self.PAUSE_THRESHOLD:
                self.clock.tick(self.framerate)
                self.update()
                self.consume_events()
                self.cycles += 1
            else:
                ev = pg.event.wait()
                if self.handle_event(ev):
                    self.cycles += 1  # add a fake cycle to force redraw

    def consume_events(self):
        if not self.quit:
            for ev in pg.event.get():
                self.handle_event(ev)
                if self.quit:
                    break

    def handle_event(self, ev):
        if ev.type == pg.QUIT:
            self.do_quit()
            return True
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.locals.K_ESCAPE:
                self.do_quit()
                return True
        elif ev.type == pg.MOUSEBUTTONUP:
            if ev.button == 4:
                self.do_speedup(1)
                return True
            elif ev.button == 5:
                self.do_speedup(-1)
                return True
            elif ev.button == 1:
                x, y = ev.pos
                self.toggle_cell_at_pixel(x, y)
                return True

    def do_quit(self):
        self.quit = True

    def do_speedup(self, value):
        self.framerate = min(100, max(self.PAUSE_THRESHOLD, self.framerate + value))

    def toggle_cell_at_pixel(self, x, y):
        board_rows, board_cols = self.board.shape
        row = y * board_rows // self.screen_height
        col = x * board_cols // self.screen_width
        self.board[row][col] = 1 - self.board[row][col]
