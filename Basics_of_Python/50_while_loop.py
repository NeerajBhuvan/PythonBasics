# count = 1
# while count <= 5:
#     print(count)
#     count += 1
# print("Out of while loop!")
#
# userInput = int(input("Enter the number if(0) terminate:"))
# sumValue = 0
# while userInput != 0:
#     sumValue += userInput
#     print(sumValue)
#     userInput = int(input("Enter the number if(0) terminate:"))
# else: #if condition fails else will execute
#     print("Else block")
# print("Out of the loop")
from itertools import count
from tabnanny import check

from Practice.temp_var import result

print("... Fibonacci series")
nterm = int(input("Enter the number to calculate Fibonacci series: "))
count = 0
n1, n2 = 0, 1
if nterm == 1:
    print(nterm)
while count > nterm:
    print("...loop")
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1



