import os


def addition(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


def subtraction(a, b):
    result = a - b
    print(f"{a} - {b} = {result}")
    return result


def multiplication(a, b):
    result = a * b
    print(f"{a} * {b} = {result}")
    return result


def division(a, b):
    result = a / b
    print(f"{a} / {b} = {result}")
    return result


def calculation(first_number):
    operator = input("Pick an operator(+, -, *, /): ").lower()
    next_number = float(input("Enter the next number: "))
    fetch_operator = {
        "+": addition,
        "-": subtraction,
        "*": multiplication,
        "/": division
    }
    output = fetch_operator[operator](first_number, next_number)
    decision = input(f"Enter 'y' to continue calculation with {output} or 'n' to start new calculation or 'x' to exit: ")
    if decision == "y":
        return calculation(output) #recursion
    else:
        return decision


continue_calc = True
while continue_calc:
    first_number_input = float(input("Enter the first number: "))
    check_decision = calculation(first_number_input)
    if check_decision == "n":
        os.system('cls')
    else:
        continue_calc = False
print("GoodBye!!!")
