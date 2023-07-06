# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?") #Outside Loop, Prints the string inside of the print function
answer = input() #Outside Loop, assigns the user input to the "answer function" 

while answer != "Paris": #Beginning of Loop, indented code below will run when the value of the "answer" variable is not "Paris"
  print("Incorrect! Try again.") #Inside the Loop, will only run if the conditions of the loop are met, prints the string inside of the function to the console
  answer = input("What is the capital of France?") #Inside the loop, will only run if the conditions of the loop are ment, prompts the user with a question, asks for input, and assigns the input to the "answer" varibale

print("Correct!") #Outside of loop, will run condition of loop is false and loop will not run, prints string "Correct!" to the console

# Example code 2

counter = 1 #Outside Loop, Assigns int 1 to variable "counter"

while counter < 5: #Beginning of loop, will only run when value of "counter" variable is less than 5
  print("This code is inside the loop") #Inside loop, will only run when condition of loop is true, prints the string inside of the function to the console
  counter += 1 #Adds 1 to the value of the "counter" variable and assigns the new value to the variable. When the statement has run enough times, the condition in the loop will not be satisfied and the loop will stop running
