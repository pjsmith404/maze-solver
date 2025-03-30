from random import randrange

from window import Window, Line, Point

def main():
    print("Running")
    win = Window(800, 600)
    for i in range(10):
        line = Line(Point(randrange(800),randrange(600)), Point(randrange(800),randrange(600)))
        win.draw_line(line, "red")
    win.wait_for_close()

if __name__ == "__main__":
    main()
