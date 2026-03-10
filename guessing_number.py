# The computer picks a random number, and you keep guessing until you get it right. After each guess, the program
# tells you whether your guess is too high, too low, or correct
# Learning points: Loops, conditionals, Random numbers and input handling

import random as rm

random_num = rm.randint(1, 50)
attempts = 0

print("I am thinking of a number between 1 and 50")

while True:
  guess = int(input("Your guess: "))
  attempts += 1

  if guess < random_num:
      print("Too low!")
  elif guess > random_num:
      print("Too high")
  else:
      print(f"Correct! You got it in {attempts} attempts")
      break