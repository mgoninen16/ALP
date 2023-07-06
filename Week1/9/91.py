# Example Code 1

def say_hi(): #Defining subroutine "say_hi"
  print("Why hello there!") #will print the string in the function when subroutine is called

def offer_drink(): #Defining subroutine "offer_drink"
  print("Would you care for a spot of tea?") #will print the string in the function when subroutine is called

def offer_food(): #Defining subroutine "offer_food"
  print("Biscuit?") #will print the string in the function when subroutine is called

def say_bye(): #Defining subroutine "say_bye"
  print("Cheerio then.") #will print the string in the function when subroutine is called


offer_drink() #Calls offer_drink(), will print the string inside of the subroutine
say_hi() #Calls say_hi(), will print the string inside of the subroutine
offer_food() #Calls offer_food(), will print the string inside of the subroutine

# Example code 2
def maths1(): #defines subroutine "maths1"
  num1 = 50 #Assigns int 50 to variable "num1"
  num2 = 5 #Assigns int 5 to variable "num2"
  return num1 + num2 #returns the sum of num1 and num2 (55)

def maths2(): #defines subroutine "maths2"
  num1 = 50 #Assigns int 50 to variable "num1"
  num2 = 5 #Assigns int 5 to variable "num2"
  return num1 - num2 #Returns the difference of num1 and num2 (45)

def maths3(): #defines subroutine "maths3"
  num1 = 50 #Assigns int 50 to variable "num1"
  num2 = 5 #Assigns int 5 to variable "num2"
  return num1 * num2 #Returns the product of num1 and num2 (250)

outputNum = maths2() #Assigns maths2() subroutine to variable "outputNum"
print(outputNum) #Prints variable "outputNum" (would print 45)

# Example Code 3
def location(country): #Defines subroutine "location" with the argument "country"
  print("I am from " + country #Prints "I am from " + whatever the users passes for the argument "country"


location("Brazil") #Calls the location subroutine, printing "I am from Brazil"

