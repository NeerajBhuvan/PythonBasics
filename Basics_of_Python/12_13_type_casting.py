#integer to string
length = len(input("Enter your Name: "))
print("You name has " + str(length) + " Characters")

#string to integer
var1 = "20"
print(10 + int(var1))

#integer to float
print(50 + float(var1))

#float to integer
var2 = 50 + float(var1)
print(int(var2) + 30)

#integer, float to String
var3 = 15
var4 = str(var3) + str(var2)
print(var4, type(var4))

#Assignment2
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
print("Addition of two numbers are: " + str(int(num1) + int(num2)))

#Assignment3
inputNum = input("Enter a two digit number: ")
print("Sum of two digit number is " + str(int(inputNum[0]) + int(inputNum[1])))
