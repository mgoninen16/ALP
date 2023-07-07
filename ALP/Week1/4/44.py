# Program to calculate the area of a rectangle

# Get input for height & width. Convert to integers and store in variables

# Calculate the area & store the result in the area variable

# Output the area variable (converted to string)

#I did all of the required and challenged exercises. You can set some of my code as comments to view the individual calculators.

print("Rectangular Area Calculator:")
print()
length = int(input("Welcome to the rectangular area calculator! Please input the length of the rectangle."))
print()
width = int(input("Now, please input the width of the rectangle."))
print()
area = str(length * width)
print("The area of the rectangle is " + area)
print()


'''
Extra Challenges
Perimeter Calc
Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle. 
'''

print("Rectangular Perimeter Calculator:")
print()
length = int(input("Welcome to the rectangular perimeter calculator! Please input the length of the rectangle."))
print()
width = int(input("Now, please input the width of the rectangle."))
print()
perimeter = str((length * 2) + (width * 2))
print("The perimeter of the rectangle is " + perimeter)
print()

'''
Restaurant Tip Calculator 
Create a program that allows the user to enter the price of a meal at a restaurant. The program calculates the amount of the tip to be paid at 20%. The tip and total price are then displayed separately.
'''

print("Restaurant Tip Calculator:")
print()
price = input("Welcome to the restaurant tip calculator! Please input the price of the meal you would like to find a tip for.")
print()
tip = (float(price) * 0.2)
print("The tip is " + str(tip) + ".")
total = float(price) + tip
print("The total is " + str(total) + ".")


'''
Volume and Surface Calc 
Create a program that allows the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. 
'''

print("Volume and Surface Area Calculator:")
print()
height = input("Welcome to the Volume and Surface Area Calculator! Please input the height of the object.")
print()
width = input("Next, please input the width.")
print()
length = input("Finally, please input the length.")
print()
volume = int(height) * int(width) * int(length)
surfaceArea = (2 * ((int(length) * int(width)) + (int(length) * int(height)) + (int(width) * int(height))))
print("The volume is " + str(volume) + ". The surface area is " + str(surfaceArea) + ".")