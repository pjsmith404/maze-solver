from random import randrange

from graphics import Window, Line, Point, Cell

def main():
    print("Running")

    width = 800
    height = 600
    cell_size = 50

    win = Window(width, height)

    for i in range(cell_size, width - cell_size, cell_size):
        for j in range(cell_size, height - cell_size, cell_size):
            cell = Cell(win)
            cell.draw(i, j, i+cell_size, j+cell_size)

    win.wait_for_close()

if __name__ == "__main__":
    main()
