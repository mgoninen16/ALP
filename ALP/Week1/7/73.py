'''
In the modify tasks, you are given some starter code. Use the instructions below to make changes to the code. Comment your changes to explain what you have done.

Run the program to see how it works.
Adapt the code to:

1. Get user input into the number variable.
2. Change the print statement so it outputs 'number' multiplied by 'counter' equals 'product'
3. Make the counter increase by 2 every loop
4. Add a line once the loop has finished to output 'The loop has finished' '''


number = int(input("Please input a number"))
counter = 1

while counter < 13:
  print(str(number) + " multiplied by " + str(counter) + " equals " + str(number * counter))
  counter += 2

print("The loop has finished")


#Task 3b

number = int(input("Please enter a number to view it's times table\n"))
counter = 1
print()
while counter < 13:
  print(str(number) + " multiplied by " + str(counter) + " equals " + str(number * counter))
  counter += 1
print("\nHere is the times table for the number " + str(number) + ". The loop has finished.")