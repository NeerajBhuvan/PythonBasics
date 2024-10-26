class Student: # bundling data/attributes and methods into a single entity class
    def __init__(self, name, rollno, age):
        self.name = name  # public instance variable/attribute
        self._rollno = rollno  # protected instance variable/attribute
        self.__age = age # private instance variable/attribute

    def public_method(self):  # public instance method
        print(f"My name is {self.name}")

    # Getter method:
    def get_age(self):
        return self.__age

    # Setter method:
    def set_age(self, age_value):
        if self.__age < 18:
            print("Invalid age! Age should be more than 18")
        else:
            self.__age = age_value

    def __private_method(self): # private instance method
        print(f"My name is {self.name} and I'm {self.__age} years old. My roll no is {self._rollno}")

    def get_private_method(self):
        self.__private_method()

s1 = Student("Neeraj", 1001, 23)

# Access/modify private attribute/method using getters and setters
print(s1.get_age())
s1.set_age(25)
print(s1.get_age())
s1.get_private_method()

# Access private attribute/method using Name Mangling
# print(dir(s1))
# s1._Student__private_method()


