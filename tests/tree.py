#!/usr/bin/env python3


import sys
sys.path.append('../')
from canvas import TurtleCanvas


# Idk where this is from, not mine
def tree(canvas, levels, trunk_len, angle, shrink_factor):
    if levels <= 0:
        return
    canvas.forward(trunk_len)
    canvas.right(angle)
    tree(canvas, levels - 1, trunk_len * shrink_factor, angle, shrink_factor)
    canvas.left(angle * 2)
    tree(canvas, levels - 1, trunk_len * shrink_factor, angle, shrink_factor)
    canvas.right(angle)
    canvas.backwards(trunk_len)


def main():
    canvas = TurtleCanvas(150, 150)
    canvas.goto(0, 75)
    tree(canvas, 5, 50, 90, 0.6)

    canvas.save_to_ppm_file('tree.ppm', folder='../test-results/')


if __name__ == '__main__':
    main()
