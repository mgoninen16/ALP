# Example code 1

age = 18 
 
if age > 18: 
 print("You are old enough to drive") 

# Prediction: I do not think this will work, because age is not greater than 18 because the age is 18 itself. Since there is no elif or else selection, nothing will print.

# Example code 2

num1 = 1337 
 
if num1 == 10: 
  print("This text is output because the condition was true") 
else:
  print("This text is output because the condition was false") 

# Prediction: The "else" branch will print because the use of the comparison operator shows that num1 == 1337, not 10. The condition is not met.

# Example code 3

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# Prediction: If the user correctly inputs 5, then the computer will print "Correct"! If the guess is less than 5, then "Too Low!" will be printed. If the guess is greater than 5, then "Too High!" will be printed.