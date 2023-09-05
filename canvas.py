import sys


class TurtleCanvas():
    def __init__(self, w, h, bg_color):
        self.width = w
        self.height = h
        self.pixels = [bg_color] * (w * h)

    def save_to_ppm_file(self, name):
        with open(name, 'w') as f:
            f.write(f'P3\n{self.width} {self.height}\n255\n')
            for pixel in self.pixels:
                r = pixel >> (8 * 2) & 0xFF
                g = pixel >> (8 * 1) & 0xFF
                b = pixel >> (8 * 0) & 0xFF
                f.write(f'{r} {g} {b}\n')

    def draw_pixel(self, x, y, color):
        if x >= self.width or y >= self.height:
            print(f'{x} {y} not in {self.width}x{self.height}')
            return
        self.pixels[x * self.width + y] = color
