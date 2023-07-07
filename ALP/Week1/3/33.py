name = input("What is your name? We want to know if you like progamming!")
#In line 1, I assigned the "name" variable to an input. I put a prompt in that asks the user for their name because the program wants to know if they like programming.
print()
answer = input("Do you like programming " + name + "?")
#In line 4, I combined the "Do you like programming?" question and the answer = input() function. The input function will now ask a prompt, itself, rather than relying on a separate print function to ask the question.
print("Great, " + name + "! You said " + answer + "!")
#The answer printed on line 6 includes the name and answer inputs.
print("Let's learn some Python today")