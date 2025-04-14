"""
Abstract Classes and Abstract Methods
Abstract Class
An abstract class is a class that:

Cannot be instantiated directly
Serves as a blueprint for other classes
Contains at least one abstract method
Is created using ABC (Abstract Base Class) in Python
Abstract Methods
Abstract methods are:

Methods declared in an abstract class with the @abstractmethod decorator
Have no implementation in the abstract class (or minimal implementation)
Must be implemented by any non-abstract child class
"""

"""
Abstract Classes in Real-World Scenarios
Abstract classes are powerful tools in object-oriented programming that provide several key benefits in real-world applications:

1. Creating Standardized Frameworks
Software frameworks often use abstract classes to define interfaces that developers must implement. For example:

UI Frameworks: Abstract Component classes that require concrete implementations to handle rendering and events
Game Development: Abstract GameObject classes that require all game entities to implement update() and render() methods
2. Ensuring Consistent Behavior
Abstract classes guarantee that certain critical functionality exists in all derived classes:

Payment Processing Systems: An abstract PaymentProcessor class ensures every payment method (credit card, PayPal, etc.) implements authorize(), charge(), and refund()
Database Access: An abstract DatabaseConnector requiring all database drivers to implement connection and query methods
3. Facilitating Polymorphism
Abstract classes enable writing code that works with multiple implementations:

Device Drivers: Operating systems use abstract device interfaces so applications can work with any compatible hardware
Plugin Systems: Applications can load various plugins that all conform to an abstract interface
4. Preventing Incomplete Implementations
By making a class abstract, you prevent creating objects from classes that aren't fully implemented, avoiding runtime errors.

In your example, the Vehicle class ensures that any vehicle type (car, motorcycle, boat) must implement basic movement functionality, making the system more robust and maintainable.
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("Driving!!!!")

    def stop(self): 
        print("Stopping!!!!")


class Boat(Vehicle):
    def go(self):
        print("Driving!!!!")

    def stop(self): 
        print("Stopping!!!!")



car = Car()
car.stop()

boat = Boat()
boat.go()
