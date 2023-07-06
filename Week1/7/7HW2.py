'''
Cubes Cubes Cubes
------------------

The cubed number sequence starts: 1, 8, 27, 64, 125...
Write a program that:
		 	 	 		
Asks the user to input a number.
Display N numbers in the cubed sequence according to user input. 
				
You may use any of the methods taught in class. The promt is quite brief so there is room for interpretation as to how to accomplish this task. 

'''
#Start coding below this line
print("Welcome Cubes Cubes Cubes! \n")
number = int(input("Please input a number to \"n\" see that many terms of the cubed number sequence: "))

counter = 1
while counter <= number:
  print(str(counter ** 3))
  counter += 1