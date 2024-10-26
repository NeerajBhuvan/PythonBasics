from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, tires):
        self.no_of_tires = tires

    @abstractmethod
    def start(self):
        pass

    def display(self):
        print("This message is from Abstract Vehicle class")