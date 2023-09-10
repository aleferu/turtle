import math
import os


class TurtleCanvas():
    def __init__(self, w, h, bg_color=0x000000, pen_color=0xFFFFFF):
        self.width = w
        self.height = h
        self.pixels = [bg_color] * (w * h)
        self.cursor = 0
        self.is_pen_down = True
        self.angle = 0
        self.color = pen_color

    def save_to_ppm_file(self, file_name, folder):
        if not os.path.exists(folder):
            os.mkdir(folder)
        target = folder + file_name
        with open(target, 'w') as f:
            f.write(f'P3\n{self.width} {self.height}\n255\n')
            for pixel in self.pixels:
                r = pixel >> (8 * 2) & 0xFF
                g = pixel >> (8 * 1) & 0xFF
                b = pixel >> (8 * 0) & 0xFF
                f.write(f'{r} {g} {b}\n')

    def up(self):
        self.is_pen_down = False

    def down(self):
        self.is_pen_down = True

    def right(self, turning_angle):
        self.angle -= turning_angle

    def left(self, turning_angle):
        self.angle += turning_angle

    # geeksforgeeks.org/dda-line-generation-algorithm-computer-graphics/
    # Modified DDA algorithm, had to modify it for my case or it didn't work
    def forward(self, distance):
        x0 = self.cursor % self.width
        y0 = self.cursor // self.width
        rads = math.radians(self.angle)
        x1 = round(x0 + distance * math.cos(rads))
        y1 = round(y0 - distance * math.sin(rads))
        if not self.is_pen_down:
            self.goto(x1, y1)
            return
        if not (0 <= x1 < self.width and 0 <= y1 < self.height):
            print(f'Tried to draw a line that ends at({x1}, {y1}) ')
            print(f'but the canvas is {self.width}x{self.height}')
            return
        dx = abs(x0 - x1)
        dy = abs(y0 - y1)
        steps = max(dx, dy)
        if steps > 0:  # Needed so there's no division by 0
            xinc = dx / steps if x0 < x1 else - dx / steps
            yinc = dy / steps if y0 < y1 else - dy / steps
            x, y = float(x0), float(y0)
            for _ in range(steps):
                self.pixels[int(y) * self.width + int(x)] = self.color
                (x, y) = (x + xinc, y + yinc)
            self.cursor = int(y) * self.width + int(x)
        else:
            self.pixels[self.cursor] = self.color

    def backwards(self, distance):
        self.forward(-distance)

    def set_color(self, color):
        self.color = color

    def goto(self, x, y):
        if x >= self.width or y >= self.height:
            print(f'Tried to call goto({x}, {y}) ')
            print(f'but the canvas is {self.width}x{self.height}')
            return
        self.cursor = y * self.width + x

    def dot(self):
        if self.is_pen_down:
            self.pixels[self.cursor] = self.color
