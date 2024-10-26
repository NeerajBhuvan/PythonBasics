
# range(start, stop(default), step_size)

print("a...")
a = range(6)
for i in a:
    print(i)

print("b...")
b = range(1,6)
for i in b:
    print(i)

print("c...")
c = range(2,7,2)
for i in c:
    print(i)

print("d...")
d = range(10, 0, -1)
for i in d:
    print(i)

print("e...")
e = range(-1, -11, -1)
for i in e:
    print(i)

sumValue = 0
for i in range(1,101, 1):
    sumValue += i
print(sumValue)

# find even numbers from 1 to 100
evenNumber = 0
for even in range(2, 101, 2):
    evenNumber += even
# for even in range(1, 101):
#     if even % 2 == 0:
#         evenNumber += even
print(evenNumber)


# fizzBuzz interview question
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
