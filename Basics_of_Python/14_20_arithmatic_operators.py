val1 = 20
val2 = 10

# Addition
print(f"Addition: {val1 + val2}")

# Subtraction
print(f"Subtraction: {val1 - val2}")

# Multiplication
print(f"Multiplication: {val1 * val2}")

# power/Exponent
print(f"power: {val1 ** val2}") \
 \
    # Division (return float)
print(f"Division: {val1 / val2}")

# Flow Division (convert from float and returns integer)
print(f"Flow Division: {val1 // val2}")

# Modulus
print(f"Modulus: {val1 % val2}")

# PEMDAS Rule (Parenthesis, Exponent, Multiplication, Division, Addition, Subtraction)
print(f"PEMDAS Rule: {5 + 2 * (3 - 1) + 10 / 5}")

# Asssignment Calculate_BMI
# weight = int(input("Enter the weight in kg: "))
# height = float(input("Enter the height in m: "))
# calculated_BMI = weight / (height ** 2)
# print("calculated BMI for given values is: " + str(calculated_BMI))

# Lec-20 Assignment
weight = int(input("Enter the weight in kg: "))
height = float(input("Enter the height in m: "))
calculated_BMI = int(weight / (height ** 2))
print("calculated BMI for the person in weight " + str(weight) + " and in height " + str(height) + " is " + str(
    calculated_BMI))
