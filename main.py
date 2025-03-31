from random import randrange
from time import sleep

from graphics import Window, Line, Point, Cell

def main():
    print("Running")

    width = 800
    height = 600
    cell_size = 50

    win = Window(width, height)

    cells = []
    for i in range(cell_size, width - cell_size, cell_size):
        for j in range(cell_size, height - cell_size, cell_size):
            cell = Cell(win)
            cells.append(cell)
            cell.draw(i, j, i+cell_size, j+cell_size)

    cells[0].draw_move(cells[1])
    sleep(1)
    cells[1].draw_move(cells[2])
    cells[2].draw_move(cells[1], True)

    win.wait_for_close()

if __name__ == "__main__":
    main()
