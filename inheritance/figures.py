import math

class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError("Метод area() має бути реалізований у підкласі!")

    def perimeter(self):
        raise NotImplementedError("Метод perimeter() має бути реалізований у підкласі!")

    def info(self):
        print(f"Фігура: {self.__class__.__name__}, колір: {self.color}")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def info(self):
        super().info()
        print(f"→ Радіус: {self.radius}")
        print(f"→ Площа: {self.area():.2f}")
        print(f"→ Довжина кола (периметр): {self.perimeter():.2f}")
        print("-" * 40)


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def info(self):
        super().info()
        print(f"→ Ширина: {self.width}, Висота: {self.height}")
        print(f"→ Площа: {self.area()}")
        print(f"→ Периметр: {self.perimeter()}")
        print("-" * 40)


class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)

    def info(self):
        super().info()
        print(f"→ Сторона квадрата: {self.width}")
        print("-" * 40)


class Triangle(Shape):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def info(self):
        super().info()
        print(f"→ Сторони: {self.a}, {self.b}, {self.c}")
        print(f"→ Площа: {self.area():.2f}")
        print(f"→ Периметр: {self.perimeter():.2f}")
        print("-" * 40)


circle = Circle("червоний", 5)
rectangle = Rectangle("синій", 4, 6)
square = Square("зелений", 3)
triangle = Triangle("жовтий", 3, 4, 5)


circle.info()
rectangle.info()
square.info()
triangle.info()
