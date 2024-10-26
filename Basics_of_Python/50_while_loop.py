count = 1
while count <= 5:
    print(count)
    count += 1
print("Out of while loop!")

userInput = int(input("Enter the number if(0) terminate:"))
sumValue = 0
while userInput != 0:
    sumValue += userInput
    print(sumValue)
    userInput = int(input("Enter the number if(0) terminate:"))
else: #if condition fails else will execute
    print("Else block")
print("Out of the loop")
