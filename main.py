
#call absract method first
from abc import ABC, abstractmethod

#then create abstract class
class Engine(ABC):
#then abstractmethod above a method to create abstract method
    @abstractmethod
    def start(self):
        pass

#two child classes that prints different messages
#1
class GasEngine(Engine):
    def start(self):
        print("Gas Engine")

#2
class ElectricEngine(Engine):
    def start(self):
        print("Electric Engine")

#Then a vehicle class that has model name and Engine object. Stores engine using composition
class Vehicle:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

#return with str
    def __str__(self):
        return self.model
#return with list,tuple type = repr
    def __repr__(self):
        return f"Model: {self.model}, {type(self.engine).__name__}"
#with eq
    def __eq__(self, other: "Vehicle") -> bool:
        return self.model == other.model and type(self.engine) == type(other.engine)


v1 = Vehicle(model = "Zx6r", engine = GasEngine())
v2 = Vehicle(model = "GXSR", engine = ElectricEngine())
v1.engine.start()
v2.engine.start()