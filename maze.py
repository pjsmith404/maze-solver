from time import sleep
import random

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
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

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
        if self._win is None:
            return

        x1 = self._x1 * (i + 1)
        y1 = self._y1 * (j + 1)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False

        self._draw_cell(0, 0)
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]

        current_cell.visited = True

        while True:
            to_visit = []

            above = (i, j-1, "above")
            below = (i, j+1, "below")
            left = (i-1, j, "left")
            right = (i+1, j, "right")

            adjacent = [above, below, left, right]

            for adj in adjacent:
                k, l, direction = adj
                if k >= 0 and k < self._num_cols and l >= 0 and l < self._num_rows:
                    if self._cells[k][l].visited == False:
                        to_visit.append(adj)

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            k, l, direction = to_visit[random.randrange(len(to_visit))]
            chosen_cell = self._cells[k][l]

            if direction == "above":
                current_cell.has_top_wall = False
                chosen_cell.has_bottom_wall = False
            if direction == "below":
                current_cell.has_bottom_wall = False
                chosen_cell.has_top_wall = False
            if direction == "left":
                current_cell.has_left_wall = False
                chosen_cell.has_right_wall = False
            if direction == "right":
                current_cell.has_right_wall = False
                chosen_cell.has_left_wall = False

            self._draw_cell(i, j)
            self._draw_cell(k, l)

            self._break_walls_r(k, l)

