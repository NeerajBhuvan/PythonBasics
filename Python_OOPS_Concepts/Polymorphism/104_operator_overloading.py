from operator import truediv


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other): #gt method overloads getter than (>) operator
        if self.age > other.age:
            return True
        else:
            return False

p1 = Person("Varsha", 25)
p2 = Person("Neeraj", 29)

if p1 > p2:
    print(f"{p1.name} need to pay a bill")
else:
    print(f"{p2.name} need to pay a bill")

class ComplexNumber:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, other): #add method overloads additional (+) operator
        return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"

c1 = ComplexNumber(2, 7)
c2 = ComplexNumber(5, 3)
print(c1 + c2)