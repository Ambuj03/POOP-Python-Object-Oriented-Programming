class Animal:

    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"The {self.name} is eating")

    def sleep(self):
        print(f"The {self.name} is sleeping")

class prey(Animal):
    def flee(self):
        print(f"The {self.name} is fleeing")

class predator(Animal):
    def hunt(self):
        print(f"The {self.name} is hunting")

class Dear(prey):
    pass

class Lion(predator):
    pass

class Fish(prey,predator):
    pass


dear = Dear("Hiran")
lion = Lion("Sher Khaan")
fish = Fish("Nemo")

lion.hunt()