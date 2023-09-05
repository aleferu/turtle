#!/usr/bin/env python3


from canvas import TurtleCanvas


def main():
    canvas = TurtleCanvas(2, 2, 0x000000)
    canvas.draw_pixel(0, 1, 0xff0000)
    canvas.save_to_ppm_file('test.ppm')


if __name__ == '__main__':
    main()
