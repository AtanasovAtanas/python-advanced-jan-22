class Square:
    def __init__(self, side):
        self.side = side


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class AreaCalculator:

    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            if isinstance(shape, Square):
                total += shape.side * shape.side
            elif isinstance(shape, Rectangle):
                total += shape.width * shape.height

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6), Square(3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
