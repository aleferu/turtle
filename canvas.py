
class TurtleCanvas():
    def __init__(self, w, h, bg_color=0x000000, pen_color=0xFFFFFF):
        self.width = w
        self.height = h
        self.pixels = [bg_color] * (w * h)
        self.cursor = 0
        self.pen_down = True
        self.angle = 0
        self.color = pen_color

    def save_to_ppm_file(self, name):
        with open(name, 'w') as f:
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
        self.angle += turning_angle

    def left(self, turning_angle):
        self.angle -= turning_angle

    def forward(self, steps):
        # TODO: implement DDA algorithm?
        pass

    def backwards(self, steps):
        # TODO: Maybe self.forward(-steps) would work
        pass

    def set_color(self, color):
        self.color = color

    def goto(self, x, y):
        if x >= self.width or y >= self.height:
            print(f'Tried to call goto({x}, {y}) ')
            print(f'but the canvas is {self.width}x{self.height}')
            return
        self.cursor = x * self.width + y

    def dot(self):
        if self.is_pen_down:
            self.pixels[self.cursor] = self.color
