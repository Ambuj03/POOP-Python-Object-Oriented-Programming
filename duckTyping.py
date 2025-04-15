# "Duck Typing" :- Another way to acheive polymorphism besides inheritance
#                  Object must have the minimum neccessary attributes/methods
#                  "If it looks like a duck, quacks like a duck, it must be a duck"

class Animal:
    alive = True


class Dog (Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    def speak(self):
        print("HONK!")

# By duck typing I made the car an animal well it could be called an Animal since it has similar characs

dog = Dog()
cat = Cat()
car = Car()

print(dog.alive)