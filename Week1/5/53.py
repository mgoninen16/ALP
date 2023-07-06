# Starter Code. Task: Make comments to explain what the each line of code in the program does.

number = 5 #Sets the variable "number" equal to the int 5
print("I have thought of a number between 1 and 10") #Prints the words in the quotes to the console
guess = int(input("Can you guess what it is?")) #Asks the user "Can you guess what it is?", prompts for an input, and saves that input as an int to the variable "guess".


if guess < number: 
  print("Too Low!") #For lines 8 and 9, If the number inputted by the user is less than 5, the console will output: "Too Low!"
if guess > number:
  print("Too High!") #For lines 10 and 11, If the number inputted by the user is greater than 5, the console will output: "Too High!"

