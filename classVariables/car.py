class Car:
    def __init__(self,name,color,year):
        self.name = name
        self.color = color
        self.year = year
        Car.num_of_cars += 1 

    def describe(self):
        print(f" Your car {self.name} is of color {self.color} and is a {self.year} model.")

    num_of_cars = 0

