import random
from Python_Projects.hangman_stage_p3 import hangman_stages

list_words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
word = random.choice(list_words)
print(word)
guess = []
for char in word:
    guess.append('_')
print(guess)
death_count = 0
while death_count < 6:
    letter = input("guess the letter: ")
    if len(letter) != 1:
        print("Please enter a single letter!")
        continue
    if letter in guess:
        print("you already guessed this word!")
        continue
    if letter in word:
        for position in range(len(word)):
             if letter == word[position]:
                 guess[position] = letter
        print(guess)
    else:
        death_count += 1
        print(hangman_stages[death_count])
    if '_' not in guess:
        print("You Won!!!")
        break
    if death_count == 6:
        print("you lose!!!")
