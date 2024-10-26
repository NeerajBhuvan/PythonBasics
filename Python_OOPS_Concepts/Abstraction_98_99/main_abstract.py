from abstract_properties import *

print("\nBike...")
bike = Bike(2, "Green")
print(bike.no_of_tires)
bike.start()
bike.display()

print("\nScotty...")
scotty = Scotty(2)
print(scotty.no_of_tires)
scotty.start()
scotty.display()

print("\nCar...")
car = Car(4)
print(car.no_of_tires)
car.start()
car.display()