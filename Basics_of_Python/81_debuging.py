# Index error
import random
dice_numbers = ["One", "Two", "Three", "Four", "Five", "Six"]
dice_num = random.randint(1,6) #Here is the issue if 6 it will throw error(IndexError: list index out of range) (1,2,3,4,5) => (0,1,2,3,4,5)
print(dice_numbers[dice_num])

#Conditional error
year = int(input("Enter the year: ")) #1996
if year > 1980 and year < 1996: #here we need to give <= 1996
    print("You are a Millennial")
elif year > 1996:
    print("You are a Gen Z")

# Multiple error
age = input("How old are you? ")
# if age >= 18: #age is str
# print("You can vote at age {age}") indentation error and need to add f string

#Eqality error
a, b = 0, 0
a = int(input("Enter a: "))
b == int(input("Enter b: ")) #single equality should come
multiplication = a * b
print(multiplication)