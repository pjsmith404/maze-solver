from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_colour="black"):
        line.draw(self.__canvas, fill_colour)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_one, point_two):
        self.point_one = point_one
        self.point_two = point_two

    def draw(self, canvas, fill_colour="black"):
        canvas.create_line(
            self.point_one.x,
            self.point_one.y,
            self.point_two.x,
            self.point_two.y,
            fill=fill_colour,
            width=2
        )

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        top_left_point = Point(x1, y1)
        top_right_point = Point(x2, y1)
        bottom_left_point = Point(x1, y2)
        bottom_right_point = Point(x2, y2)

        if self.has_left_wall:
            self._win.draw_line(Line(top_left_point, bottom_left_point))
        if self.has_right_wall:
            self._win.draw_line(Line(top_right_point, bottom_right_point))
        if self.has_top_wall:
            self._win.draw_line(Line(top_left_point, top_right_point))
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_left_point, bottom_right_point))

    def get_centre(self):
        centre_x = (self._x1 + self._x2) / 2
        centre_y = (self._y1 + self._y2) / 2

        return (centre_x, centre_y)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return

        fill_colour = "red"
        if undo:
            fill_colour = "grey"

        self_centre = Point(*self.get_centre())
        to_cell_centre = Point(*to_cell.get_centre())
        self._win.draw_line(Line(self_centre, to_cell_centre), fill_colour)

