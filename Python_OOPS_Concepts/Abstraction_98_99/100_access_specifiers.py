class Student:
    def __init__(self, name, rollno, age):
        self.name = name  # public instance variable/attribute
        self._rollno = rollno  # protected instance variable/attribute
        self.__age = age # private instance variable/attribute

    def public_method(self):  # public instance method
        print(f"My name is {self.name}")

    def __private_method(self): # private instance method
        print(f"My name is {self.name} and I'm {self.__age} years old. My roll no is {self._rollno}")


class Course(Student):
    def __init__(self, name, rollno, age):
        super().__init__(name, rollno, age)

    def protected_method(self):  # protected instance method
        print(f"My name is {self.name} and my roll no is {self._rollno}")


# s1 = Student("Neeraj")
# s1.public_method()

c1 = Course("Neeraj", 1001, 23)
c1.protected_method()
# print(c1.__age) #AttributeError: 'Course' object has no attribute '__age'
# c1.private_method() #AttributeError: 'Course' object has no attribute 'private_method'. Did you mean: 'protected_method'?

s1 = Student("Neeraj", 1001, 23)
print(dir(s1)) #Name Mangling
s1._Student__private_method()
