
class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def count_surface_area(self):
        return self.height * self.width


class Square(Rectangle):
    def __init__(self, sideLength):
        super().__init__(sideLength, sideLength)


class Cube():
    def __init__(self, square):
        self.square = square
        self.height = square.height

    def count_surface_area(self):
        return self.square.count_surface_area() * 6

    def count_volume(self):
        return self.square.count_surface_area() * self.height


class Cuboid():
    def __init__(self, figure, height):
        self.base = figure
        self.height = height

    def count_volume(self):
        return self.base.count_surface_area() * self.height

    def count_surface_area(self):
        return 2 * self.base.count_surface_area() + 2 * self.height * self.base.width + 2 * self.height * self.base.height



cuboid = Cuboid(Rectangle(4, 2), 4)

print(cuboid.count_surface_area())


