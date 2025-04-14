class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking WOOF! WOOF!")

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("Tommy")
cat = Cat("Billi")
mouse = Mouse("Mushak")

dog.bark()
