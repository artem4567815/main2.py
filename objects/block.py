class Block:
    def __init__(self, c, image, color):
        self.image = image
        self.color = color
        self.canvas = c

    @property
    def x(self):
        return self.canvas.coords(self.image)[0]

    @property
    def y(self):
        return self.canvas.coords(self.image)[1]