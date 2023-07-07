### Example Code 1

fName = "Mr"
lName = "Colley"

print(fName)

# Identify a variable in the code
 # Answer: fName, lName

# Identify a string in the code
 # Answer: "Mr", "Colley"

# Line 4 is changed to lName = "Thorpe".  How does this affect the output?
 #Answer: The print statement on line 6 would not be changed, because that print function is printing the value of the variable fName, which is not changed. If another print command calls lName, then the string "Thorpe" would print rather than "Colley".

# Line 3 is changed to fName = "Mrs". How does this affect the output?
 # Answer: In this case, the print statement on line 6 would change to "Mrs", since the value of the variable (fName) being called is changed from "Mr" to "Mrs".


### Example Code 2

num1 = 20
num2 = 5

total1 = num1 + 15
total2 = num2 * 2
total3 = num1 - num2

print(total3)

# What will be output by the program?
 # Answer: 15. total1 = 35, total2 = 10, total3 = 20 - 5


### Example Code 3

name1 = "Ross" 
name2 = "Monica" 
name3 = "Joey" 
name4 = "Rachel" 
name5 = "Chandler" 
 
print(name1 + " and " + name4) 
print(name3) 
 
name3 = "Phoebe" 


# How many variables are used in the program?
 # Answer: 5 variables are used in the program (one for each name).

# What would be the impact of changing  print(name1, " and ", name4) to print(name1, " and ", name5) ?
 # Answer: The new output of this print function would be "Ross and Chandler", as it calls variables name1 and name5.

# What is the purpose of the '+' symbol in  print(name1, " and ", name4) 
 # Answer: The + symbol combines the value of the variables (strings) with the " and " string in order to print one string with all values combined: "Ross and Rachel" is printed.

# The line  print(name3) is added to the end of the code.  Explain what it will do.
 # Answer: The line print(name3) will print the most recent value of the variable (name3). In this case, it will print the string "Phoebe". It will NOT pring the string "Joey", because name3 is changed to "Phoebe" before the print function would print the value of the variable.