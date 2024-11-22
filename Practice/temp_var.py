def swap_variable(a, b):
    temp = a
    a = b
    b = temp
    return f"The swaped value of a is {a} and b is {b}"

result = swap_variable(10, 20)
print(result)