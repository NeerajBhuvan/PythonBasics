import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
inputIndex = [rock, paper, scissors]
userChoice = int(input("Enter the value 0 or 1 or 2 (0-Rock, 1-Paper, 2-Scissor): "))
if userChoice >= 0 and userChoice <= 2:
    print(f"User Choice: \n{inputIndex[userChoice]}")
    computerChoice = random.randint(0, 2)
    print(f"Computer Choice: \n{inputIndex[computerChoice]}")
    if userChoice == computerChoice:
        print("Game Draw!")
    elif userChoice > computerChoice:
        if userChoice == 2 and computerChoice == 0:
            print("You Lose!")
        else:
            print("You Won!")
    elif computerChoice > userChoice:
        if computerChoice == 2 and userChoice == 0:
            print("You Won!")
        else:
            print("You Lose!")
else:
    print("Invalid Input")
