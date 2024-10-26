class Duck:
    def swim(self):
        print("Duck can Swim")

    def sound(self):
        print("Duck sounds like Quack-Quack")

class Dog:
    def swim(self):
        print("Dog can Swim")

    def sound(self):
        print("Dog sounds like Woof-Woof")

class DynamicTyping:
    def display(self, obj):
        obj.swim() #dynamically changing object/class
        obj.sound() #dynamically changing object/class

duck = Duck()
dog = Dog()
dynamic_typing = DynamicTyping()
dynamic_typing.display(duck)
dynamic_typing.display(dog)
