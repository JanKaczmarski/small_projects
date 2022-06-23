class Rectangle():
    def init(self, width, length):
        self.width = width
        self.length = length
    def count_surface_area(self):
        return self.width * self.length

class Square(Rectangle):
    def init(self, sideLength):
        super().init(sideLength, sideLength)