'''
Answer the questions

'''

# Example code:

names = ["Alex","Anita","Patrick","Atif","Sue"]

print("Enter a number for your choice.")
print("1. Show all")
print("2. Add name")
print("3. Show name")
print("4. Exit")
choice = int(input())

if choice == 1:
  print(names)
elif choice == 2:
  name = input("Enter the name")
  names.append(name)
elif choice == 3:
  print("Enter the index of the name")
  index = int(input())
  print(names[index])
else:
  print("Goodbye")


# What is the identifier for the list in this program?
  # Answer: The identifier is "names"

# What would happen if you choose option “3” and entered index “0”? 
  # Answer: It would print the name Alex

# What would happen if you choose option “3” and entered index “7”?
  # Answer: Error, there is no name with Index 7

# What would happen if you choose option “2” and entered the name “Stuart”?
  # Answer: It would append the name to the list

# What is the purpose of int(input()) on line 10 ?
  #Answer: For the user to enter a choice for the index of the name and save it as an int to the variable "index"