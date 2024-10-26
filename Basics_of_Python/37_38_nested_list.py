list1 = [10, 34, 90, ["Mohan", "Shyam", "Ram"], 89]
print((type(list1)))
length = len(list1)
print(list1[length - 2])
print(list1[length - 2][:])
print(list1[length - 2][:1])
print(list1[length - 2][::2])
print(list1[length - 2][-1])

list2 = [1,15,10,23,[23,34,22],42,45]
print(len(list2))

for i in list2:
    print(i)

print(list2[4])
print(list2[4][0])
print(list2[4][:])
print(list2[4][1:])
print(list2[4][:2])
print(list2[4][::2])

#matrix assignment
matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
userInput = list(input("Enter the 3*3 matrix value to modify the matric value (e.g.21): "))
rowIndex = int(userInput[0]) - 1
columnIndex = int(userInput[1]) - 1
matrix[rowIndex][columnIndex] = 'x'
print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
