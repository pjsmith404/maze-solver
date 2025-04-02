from time import sleep

from graphics import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = []

        for i in range(self._num_cols):
            cell_column = []
            for j in range(self._num_rows):
                cell_column.append(Cell(self._win))
            self._cells.append(cell_column)

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        print(i, j)
        print(self._x1, self._y1)

        x1 = self._x1 * (i + 1)
        y1 = self._y1 * (j + 1)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        print(x1, y1)
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.05)
