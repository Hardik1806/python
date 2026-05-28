from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def engine(self):
        pass
    
    @abstractmethod
    def capacity(self):
        pass
    def emission(self):
        print("releases harmful gases")
class Car(Vehicle):
    def engine(self):
        print("1500cc")
    def capacity(self):
        print("5 seater ")
class Bike(Vehicle):
    def engine(self):
        print("250cc")
    def capacity(self):
        print("2 seater")

c=Car()
c.engine()
c.capacity()
c.emission()
b=Bike()
b.engine()
b.capacity()
b.emission()
