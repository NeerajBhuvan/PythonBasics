list_syntax = []
print(type(list_syntax))

numbers = [1, 4, 2, -11, 34, 11, 9]
names = ["Neeraj", "Dhiva", "Anu"]
mix_list = [1, "Neeraj", True, 9.2]

# slicing
print("\nSlicing...!")
print(numbers[0])
print(numbers[:])
print(numbers[:6])
print(numbers[3:])
print(numbers[1:5])
print(numbers[1:5:2])
print(len(numbers))

# sorting
print("\nSorting...!")
numbers.sort()
print(numbers)
# we cannot sort the different datatype list
# mix_list.sort()
# print(mix_list)

# reverse
print("\nreverse...!")
numbers.reverse()
print(numbers)

# min & max
print("\nmin & max...!")
print(max(numbers))
print(min(numbers))

# count
print("\ncount...!")
print(mix_list.count("Neeraj"))

# To add one element in the list
print("\nAdd...!")
numbers.append(45)  # add element at end of the list and only able to add one element at a time
print(numbers)
numbers.insert(2, 33)  # insert element as per the index(first argument) and it will append not replace
print(numbers)

# add multiple element
numbers += {11,12,13}
print(numbers)
numbers.extend([31, 32, 35])  # add multiple elements at end of the list
print(numbers)

# modify
print("\nModify...!")
numbers[2] = 15  # modify/replace particular/single element based on index value
print(numbers)
numbers[3:7] = 0, 20, 0  # modify/replace multiple elements based on index value
print(numbers)

# remove (remove element based on element not index)
print("\nRemove...!")
numbers.remove(0)  # remove the given item value and multiple instance are there it will remove only the first instance right to left
print(numbers)

# remove
print("\nRemove - pop()...!")
print(numbers.pop())  # remove last value in a list and return the value
print(numbers.pop(4))  # pop also remove element based on index
print(numbers)

# remove all items in the list
print("\nclear()...!")
numbers.clear()
print(numbers)

arr = [1, 5, 10, 12, 25]
print(arr[1:3])
arr[2] = 15
arr[2:4] = [10, 15, 20]
arr.pop(0)
arr.pop(3)
print(arr)

print(arr[-len(arr)])
