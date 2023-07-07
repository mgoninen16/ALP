'''
Task - Investigate
Use comments to answer the investigate questions on the example code.

'''
# Example Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# What happens if you input the guess '2'?
  # Answer: The console will return the string "Too Low!"

# What happens if you input the guess '6'?
  # Answer: The console will return the string "Too High!"

# What happens if you input the guess '5'?
  # Answer: The console will return the string "Correct!"

# What happens if you input the guess '-5'?
  # Answer: "The console will return the string "Too Low!""

# What happens if you input the guess '0'?
  # Answer: "The console will return the string "Too Low!""

# What do the symbols '<' and '>' mean on lines 9 and 11?
  # Answer: They stand for "less than" and "greater than"

# What happens if you change line 5 to if guess = number: ?
  # Answer: You would get a syntax error. You need the to use "==" (the equality operator).

# What do you notice about each line that FOLLOWS each IF statement?
  # Answer: Each line that follows an IF statement is indented.


