import math


def add(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

# add(5, 5)
# add(2) #add() missing 1 required positional argument: 'b'

# Lec_63 calculate paint can be needed as per user input
def calculate_paint_can(height, width, coverage):
    no_of_can = math.ceil((height*width) / coverage)
    print(f"Number to cans needed to cover {coverage} area for height {height} and width {width} is {no_of_can}")

# h = float(input("Enter the height of the wall in meters: "))
# w = float(input("Enter the weight of the wall in meters: "))
# calculate_paint_can(height = h, width = w, coverage=7)

# Lec_64 Find the number is prime number or not
def find_prime_number(input):
    if input <= 1:
        print(f"{input} is not a prime number")
    else:
        prime = True
        for i in range(2, int(math.sqrt(input) + 1)):
            if input % i == 0:
                prime = False
                print(f"{input} is not a prime number")
                break
        if prime:
            print(f"{input} is a prime number")

userInput = int(input("Enter the number to find, whether the number is prime number or not: "))
find_prime_number(userInput)

