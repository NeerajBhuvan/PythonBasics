def func1(a, b):
    c = a + b
    print(c)

def func2 (a, b):
    c = a + b
    return c

def func3 (val):
    result = 5 * (val + 1)
    return result

output1 = func1(5,4) #default return None
print(output1)

output2 = func2(5, 4) #returns value for further usage
return_result = func3(output2)
print(return_result)
