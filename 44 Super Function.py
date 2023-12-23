class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
