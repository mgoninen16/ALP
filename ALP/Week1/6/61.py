# Example code 1

number = 7 # Assigns the int 7 to the variable "number"
print("I have thought of a number between 1 and 10") # Prints the string in the function to the console.
guess = int(input("Can you guess what it is?")) #Prompts the user with the string, takes user input, saves as int, assigns int to "guess" function

if guess == number: #if the int saved to "guess" == the value assigned to "number"
  print("Correct!") #the string "Correct!" is printed to the console
elif guess < number: #if the int saved to "guess" is less than "number", prints "Too Low!"
  print("Too Low!")
else: #if the condition in the if and elif statements are false
  print("Too High!") #prints "Too High!" to the console

# Example code 2

number1 = int(input("Please enter a number")) #Prompts the user with the string in the function, takes user input, saves as int, assigns int to variable "number1"
number2 = int(input("Please enter another number")) #Prompts the user with the string in the function, takes user input, saves as int, assigns into to variable "number2"

if number1 > number2: #if value assigned to "number1" is greater than value assigned to "number 2"
  print("Number 1 is bigger than number 2") #prints the string in the function to the console
elif number2 > number1: #if  value assigned to "number2"is greater than the value assigned "number1"
  print("Number 2 is bigger than number 1") #prints the string in the function to the console
else: #if the condition in the if and elif statements are false
  print("Both numbers are the same") #prints the string in the function to the console

