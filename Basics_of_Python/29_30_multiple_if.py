"""
height = int(input("Enter the height:"))
if height >= 3:
    print("You can ride!")
    age = int(input("Enter the age: "))
    totalBill = 0
    if age < 12:
        print("Your ticket price is Rs.150")
        totalBill = 150
    elif age < 18:
        print("Your ticket price is Rs.250")
        totalBill = 250
    else:
        print("Your ticket price is Rs.500")
        totalBill = 500
    needPhoto = input("Need Photo (y/n): ")
    if needPhoto == "y" or needPhoto == "Y" :
        totalBill += 50
    print(f"Your total bill is {totalBill}")
else:
    print("you can't ride")
print("Thank you, Enjoy your ride!")
"""

#Lec-30 Assignment
pizzaSize = input("What kind of pizza size you want(S/M/L): ")
pizzaPrice = 0
if pizzaSize == "S" or pizzaSize == "s":
    pizzaPrice += 100
    print(f"your small pizza price is Rs.{pizzaPrice}")
elif pizzaSize == "M" or pizzaSize == "m":
    pizzaPrice += 200
    print(f"your medium pizza price is Rs.{pizzaPrice}")
else:
    pizzaPrice += 300
    print(f"your large pizza price is Rs.{pizzaPrice}")
needPepperoni = input("need Pepperoni(y/n): ")
if needPepperoni == "Y" or needPepperoni == "y":
    if pizzaSize == "S" or pizzaSize == "s":
        print(f"Pepperoni price for your pizza is Rs.30")
        pizzaPrice += 30
    else:
        print(f"Pepperoni price for your pizza is Rs.50")
        pizzaPrice += 50
needExtraCheese = input("need Extra Cheese(y/n): ")
if needExtraCheese == "Y" or needExtraCheese == "y":
    print(f"Extra Cheese for your pizza is Rs.20")
    pizzaPrice += 20
print(f"Total price for your pizza is Rs.{pizzaPrice}")




