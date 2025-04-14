# super() -> Function used in a child class to call methods from a parent class (superclass).
#            Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"The shape is of color {self.color} and is {'filled' if self.is_filled  else 'Not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"The area of this circle is {3.14 * self.radius * self.radius}")


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


circle = Circle(color = "Red", is_filled= True, radius = 5)


square = Square(color = "Blue", is_filled = False, width=8)

circle.describe()


