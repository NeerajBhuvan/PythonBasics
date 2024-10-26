# Lec-84(Theory Class)

a = 1; print(type(a)) #<class 'int'> => so here int(1) is the instance/object of class
b = "Neeraj"; print(type(b)) #<class 'str'> => so here str("Neeraj") is the instance/object of class

# Lec-85 (class syntax)
# class Instructor: #PaselCase
#     pass
#
# instructor_1 = Instructor() #like constructor
# print(type(instructor_1)) #<class '__main__.Instructor'> => class is a user defined datatype

# Example-2
class CarDesign:
    pass

car_design_1 = CarDesign()
car_design_2 = CarDesign()

# Lec - 86 (create/modify class attributes)
# class Instructor:
#     def __init__(self, instructor_name, address):
#         self.name = instructor_name
#         self.address = address
#         self.followers = 0 #default value/argument
#
#
# instructor_1 = Instructor("Neeraj", "Chennai")
# print(instructor_1.name)
# print(instructor_1.address)
#
# instructor_2 = Instructor("Varsha", "Madurai")
# print(instructor_2.name)
# print(instructor_2.address)

# Lec - 87 (create/modify class methods)
class Instructor:
    followers = 0 #class object variable
    def __init__(self, instructor_name, address):
        self.name = instructor_name
        self.address = address

    def display_details(self, course):
        print(f"\nMy Name is {self.name} and my address is {self.address}. I am currently learning {course} programming language")

    def update_followers(self, follower_name):
        self.followers += 1
        print(f"New follower added {follower_name}, Total Followers Count: {self.followers}")


instructor_1 = Instructor("Neeraj", "Chennai")
# print(instructor_1.display_details("Python")) //while calling a function if it returns anything then use print else simply call it
instructor_1.display_details("Python")
instructor_1.update_followers("Arunya")
instructor_1.update_followers("Raja")

instructor_2 = Instructor("Varsha", "Madurai")
instructor_2.display_details("Java")
instructor_2.update_followers("Neeraj")
instructor_2.update_followers("Anu")

# Lec - 88 (Find Area and circumference of the circle using class and object)
import math
class Circle:
    pi = math.pi
    def __init__(self,radius):
        self.radius = radius

    def area_of_the_circle(self):
        area = Circle.pi * (self.radius * self.radius) # Circle.pi instead of self.pi because to differentiate constant class variable
        print(f"\nArea of the circle for given radius is: {round(area, 2)}")

    def area_of_the_circumference(self):
        circumference = 2 * Circle.pi * self.radius
        print(f"Circumference of the circle for given radius is: {round(circumference, 2)}")

find_area = Circle(3)
find_area.area_of_the_circle()
find_area.area_of_the_circumference()

find_area = Circle(5)
find_area.area_of_the_circle()
find_area.area_of_the_circumference()
