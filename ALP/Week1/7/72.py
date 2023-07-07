
number = 7
print("I'm thinking of a number, can you guess it?")
guess = int(input())
while guess != number:
  print("Wrong! Guess again!")
  guess = int(input())
print("You guessed it!")


# Give the line number where iteration starts.
  # Answer: On line 4, where the while loop starts

# What does '!=' mean?
  # Answer: Not equal

# How many variables are there in the code?
  # Answer: 2 variables "number" and "guess"

# How can you tell which lines of code are inside the loop?
  # Answer: They are indented

# How many times will the loop repeat?
  # Answer: As many times as it takes until the user inputs the correct number

# What has to happen to make the program run the last line of code?
  # Answer: The user has to guess the correct answer

# Task 3

number = 4
guess = int(input("I have a number in mind, can you guess what it is?"))
while guess != number:
  print("Incorrect! Try again!")
  guess = int(input())
print("You've got it!")