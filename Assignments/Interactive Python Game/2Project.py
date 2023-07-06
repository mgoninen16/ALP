# Players have to guess the correct number within 7 attempts
import random

name = input("Please input your name")
number = random.randint(1, 101)
guess = None
tries = 0

while guess != number:
  guess = int(input("Please input a number"))
  if guess == number:
    tries += 1
    print("Congratualations " + str(name) + ", you have correctly guessed the number in " + str(tries) + " tries.")
  elif guess < number:
    print("Too low!")
    tries += 1
  elif guess > number:
    print("Too high!")
    tries += 1