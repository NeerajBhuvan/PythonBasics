import random
print("Guess The Number")
print("Let me Think of the Number between 1 to 50: ")
random_number = random.randint(1, 50)
print(random_number)
difficulty = input("Choose the level of difficulty. Type 'ease' or 'hard': ").lower()
limit = 10

if difficulty == "hard":
    limit = 5
elif difficulty == "easy":
    limit = 10
else:
    print("Invalid difficulty input")

while limit != 0:
    print(f"You have {limit} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess == random_number:
        print(f"Your guess is right, the answer is {random_number}! You Won!!! ")
        break
    elif guess > random_number:
        limit -= 1
        if limit == 0:
            break
        else:
            print(f"Your guess is Too High! \nGuess again!")
    else:
        limit -= 1
        if limit == 0:
            break
        else:
            print(f"Your guess is Too Low! \nGuess again!")
if limit == 0:
    print("You are out of guess! You Lose!")
