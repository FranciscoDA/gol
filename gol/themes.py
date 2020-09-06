import pygame as pg

class DefaultTheme:
    def __init__(self):
        self.cell_width = 1
        self.cell_height = 1

    def cell_color(self, left, top, board, cell_row, cell_col):
        is_alive = board[cell_row][cell_col] != 0
        return (255, 255, 255) if is_alive else (0, 0, 0)

    def draw_cell(self, screen, left, top, board, cell_row, cell_col):
        color = self.cell_color(left, top, board, cell_row, cell_col)
        rect = pg.Rect(left, top, self.cell_width, self.cell_height)
        pg.draw.rect(screen, color, rect, 0)

    def draw_board(self, screen, board):
        num_rows, num_cols = board.shape
        self.cell_width = screen.get_width() // num_cols
        self.cell_height = screen.get_height() // num_rows
        for row in range(num_rows):
            for col in range(num_cols):
                left = col * self.cell_width
                top = row * self.cell_height
                self.draw_cell(screen, left, top, board, row, col)


class HeatmapTheme(DefaultTheme):
    def __init__(self):
        super().__init__()
        self.neighbours = None

    def cell_color(self, left, top, board, cell_row, cell_col):
        is_alive = board[cell_row][cell_col] != 0
        if not is_alive:
            return (0, 0, 0)
        neighbours = self.neighbours[cell_row][cell_col]
        r = 255
        g = 255 - 230 / 8 * neighbours
        b = 220 - 220 / 8 * neighbours
        return (int(r), int(g), int(b))

    def draw_board(self, screen, board):
        self.neighbours = board.get_neighbours()
        super().draw_board(screen, board)


class GridMixin:
    def draw_board(self, screen, board):
        super().draw_board(screen, board)
        color = (128, 128, 128)
        for x in range(0, screen.get_width(), self.cell_width):
            pg.draw.line(screen, color, (x, 0), (x, screen.get_height()), 1)
        for y in range(0, screen.get_width(), self.cell_height):
            pg.draw.line(screen, color, (0, y), (screen.get_width(), y), 1)
 

class GridTheme(GridMixin, DefaultTheme):
    pass


class HeatmapGridTheme(GridMixin, HeatmapTheme):
    pass

