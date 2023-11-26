import math


class Figure:
    def __init__(self, name):
        self.name = name

    def get_area(self):
        return 0

    def print_area(self):
        print(f'Фигура: {self.name}; площадь составляет: {self.get_area()}')


class Rectangle(Figure):
    """Прямоугольник. Принимает длину и ширину"""

    def __init__(self, a, b):
        self.a, self.b = a, b
        super().__init__('прямоугольник')

    def get_area(self):
        return self.a * self.b


class Circle(Figure):
    """Круг. Принимает радиус"""

    def __init__(self, radius):
        self.radius = radius
        super().__init__('круг')

    def get_area(self):
        return 3.14 * self.radius * self.radius


class RightTriangle(Figure):
    """Прямоугольный треугольник. Принимает длины катетов"""

    def __init__(self, part_1, part_2):
        self.part_1 = part_1
        self.part_2 = part_2
        super().__init__('прямоугольный треугольник')

    def get_area(self):
        return self.part_1 * self.part_2 / 2


class Trapezoid(Figure):
    """Трапеция. Принимает длины оснований и высоты"""

    def __init__(self, part_1, part_2, height):
        self.part_1 = part_1
        self.part_2 = part_2
        self.height = height
        super().__init__('трапеция')

    def get_area(self):
        return (self.part_1 + self.part_2) * self.height / 2


r = Rectangle(20, 40)
r.print_area()

c = Circle(20)
c.print_area()

tr = RightTriangle(30, 40)
tr.print_area()

tz = Trapezoid(2, 4, 3)
tz.print_area()