import string
import random

charLength = int(input("How many letters would you like in your password: "))
random_chars = random.choices(string.ascii_letters, k = charLength)
print(random_chars)

symbolLength = int(input("How many symbols would you like in your password: "))
random_symbols = random.choices(string.punctuation, k = symbolLength)
print(random_symbols)

numbers = ['0','1','2','3','4','5','6','7','8','9']
numberLength = int(input("How many numbers would you like in your password: "))
random_numbers = random.choices(numbers, k = numberLength)
print(random_numbers)
# random_numbers = []
# for i in range(numberLength):
#     random_numbers.append(str(random.randint(0, 9)))
# # random_numbers = ''.join(numbers)
# print(random_numbers)

password = random_chars + random_symbols +random_numbers
random.shuffle(password)

print(f"your generated password is: {''.join(password)}")