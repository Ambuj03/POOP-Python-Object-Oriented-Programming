"""Polymorphism means "many forms". In programming, it refers to the ability of different classes to be treated as instances of the same class through a common interface. It mainly appears in two forms:

Compile-time Polymorphism (method overloading) - Not directly supported in Python.

Run-time Polymorphism (method overriding) - Supported in Python."""

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area():
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side * self.side


shapes = [Circle(5), Square(5)]

for shape in shapes:
    print(shape.area())
