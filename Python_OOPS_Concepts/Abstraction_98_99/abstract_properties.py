from abstraction_module import Vehicle

class Bike(Vehicle):
    def __init__(self, tires, color):
        super().__init__(tires)
        self.bike_color = color

    def start(self):
        print("launch Kicker to start")

    def display(self):
        print(f"Color of the my bike is {self.bike_color}")


class Scotty(Vehicle):
    def __init__(self, tires):
        super().__init__(tires)

    def start(self):
        print("Press Quick start to start")


class Car(Vehicle):
    def __init__(self, tires):
        super().__init__(tires)

    def start(self):
        print("Enter Car key and drag upwards to start")


