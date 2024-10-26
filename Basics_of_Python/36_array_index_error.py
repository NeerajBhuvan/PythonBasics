arr1 = [1, 2, 3, 4, 5]

# print(arr1[5]) #IndexError: list index out of range

#To solve this there are two methods

# 1) Find length
arr_length = len(arr1)
print(arr1[arr_length - 1])

# 2) use negative index
print(arr1[-1])
print(arr1[-arr_length])