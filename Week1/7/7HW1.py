'''
Task Instructions
You are going to write a program called "Time Reminder"

The user has to enter a number between 0 and 23
If the number is less than 8 display a message saying "too early to get up"
If the number is less than 12 display a message saying "Good morning"
If the number is less than 14 display a message saying "Lunch time!"
If the number is less than 18 display a message saying "Good afternoon"
If the number is equal to 18 display a message saying "Tea Time"
If the number is less than 19 display a message saying "Good evening"
If the number is less than 22 display a message saying "Nearly bedtime"
If the number is 23 display a message saying "Good night!"
Any other number is met with the response “Sorry, I don’t recognise that”


You are free to use any of the methods that we have learned in class.
'''
#Start coding below this line

print("Welcome to Time Reminder! \n")
time = int(input("Please enter a number between 0 and 23 \n"))
if time < 8:
  print("Too early to get up")
elif time < 12:
  print("Good morning")
elif time < 14:
  print("Lunch time!")
elif time < 18:
   print("Good afternoon")
elif time == 18:
  print("Tea Time")
elif time <= 19:
  print("Good evening")
elif time <= 22:
  print("Nearly bedtime")
elif time == 23:
  print("Good night!")
else:
  print("Sorry, I don't recognize that")

#I had to change Time: 19 to <= because the instructions did not create a situation that would return "Good evening". I also had to change Time: 22 to <= because without this, inputting 22 would not satisfy any if/elif statements and take us to else.