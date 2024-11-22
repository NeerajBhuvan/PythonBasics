# Lec-42_for_loop
numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number ** 2)
print(f"squares of the numbers are {squares}")

# Lec-43 for_else
evenNumbers = [2, 4, 6, 8, 10]
for i in evenNumbers:
    print(i)
    # if(i % 3 == 0):
    #     print(f"{i} is divisible by 3")
    #     break
else:
    print("All the numbers are divisible by 2")  # after successful completion of for loop else will be executed

# Lec-44 Find Average Height
heights = input("Enter the heights in cm separated by comma(,): ").split(",")
sumOfHeights = 0
length = 0
for height in heights:
    sumOfHeights += int(height)
    length += 1
else:
    print(sumOfHeights)
    print(length)

averageHeight = sumOfHeights / length
print(f"Average height for given values: {round(averageHeight)}")

# Lec-45 find maximum number in a list
maxNumbers = input("Enter the numbers separated by comma(,): ").split(",")
for i in range(len(maxNumbers)):
    maxNumbers[i] = int(maxNumbers[i])
print(maxNumbers)
maxValue = maxNumbers[0]
for maxNumber in maxNumbers:
    if maxNumber > maxValue:
        maxValue = maxNumber
print(f"Maximum number of given value: {maxValue}")

arr = [29, 21, 34, 15, 19]
print(max(arr))
arr_mid = len(arr) // 2
print(arr_mid)
def find_max(arr_side):
    max_val = 0
    for i in arr_side:
        if i > max_val:
            max_val = i
    return max_val

arr_l = find_max(arr[:arr_mid])
arr_r = find_max(arr[arr_mid:])
if arr_l > arr_r:
    print(arr_l)
else:
    print(arr_r)
