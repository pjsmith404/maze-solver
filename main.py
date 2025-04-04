from graphics import Window
from maze import Maze

def main():
    print("Running")

    width = 800
    height = 600
    cell_size = 50

    win = Window(width, height)
    
    num_rows = (height - (cell_size * 2)) // cell_size
    num_cols = (width - (cell_size * 2)) // cell_size

    maze = Maze(cell_size, cell_size, num_rows, num_cols, cell_size, cell_size, win, 0)

    win.wait_for_close()

if __name__ == "__main__":
    main()
