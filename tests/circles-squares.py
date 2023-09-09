#!/usr/bin/env python3
# From https://www.codesters.com/preview/e0d4746091984000a9c939274fd29635/


import sys
sys.path.append('../')
from canvas import TurtleCanvas


def draw_square(canvas, size, color):
    canvas.set_color(color)
    for _ in range(4):
        canvas.forward(size)
        canvas.right(90)


def draw_circle(canvas, size, color):
    canvas.set_color(color)
    for _ in range(36):
        canvas.forward(size)
        canvas.right(10)


def main():
    canvas = TurtleCanvas(550, 550, bg_color=0xffffff)
    for _ in range(72):
        canvas.goto(274, 274)  # floats, am I right?
        draw_square(canvas, 100, 0xff0000)
        canvas.goto(274, 274)
        draw_circle(canvas, 20, 0x0000ff)
        canvas.right(10)

    canvas.save_to_ppm_file('circles-squares.ppm', folder='../test-results/')


if __name__ == '__main__':
    main()
