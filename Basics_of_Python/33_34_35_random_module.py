import random

a = random.randint(1, 4)
print(a)

b = random.randrange(1, 5)  # 5 won't print
print(b)

c = random.random()
print(round(c, 2))

d = random.uniform(1, 3)
print(d)

list_arr = [5, 10, 15, 20, 25]

e = random.choice(list_arr)
print(e)

print("before Suffle", list_arr)
random.shuffle(list_arr)
print("before Suffle", list_arr)

# Lec-34 assignment1 (toss)
toss = random.randint(0, 1)
if toss == 1:
    print("You got Heads")
else:
    print("You got Tails")

# Lec-35 assignment2 select random bill payer
names = input("Enter the bill payers names separated by comma(,): ").split(",")
# randomPayer = random.randint(0, len(names) - 1)
# print(f"{names[randomPayer]} need to pay a bill!")
print(f"{random.choice(names)} will pay a bill!")
