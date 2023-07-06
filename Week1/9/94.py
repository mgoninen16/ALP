def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

number1 = int(input("Please input the first number that you would like to perform an operation on."))
number2 = int(input("\nPlease input the second number that you would like to perform an operation on."))
operationNumber = int(input("\nFinally, please signify which operation you would like to perform. Addition is 1, Subtraction is 2, Multiplication is 3, Division is 4."))

if operationNumber == 1:
  result = add(number1, number2)
  operation = "addition"
elif operationNumber == 2:
  result = subtract(number1, number2)
  operation = "subtraction"
elif operationNumber == 3:
  result = multiply(number1, number2)
  operation = "multiplication"
elif operationNumber == 4:
  result = divide(number1, number2)
  operation = "division"
else:
  print("Please try again and enter a valid operation number")

print("\nThe result of " + operation + " between " + str(number1) + " and " + str(number2) + " is " + str(result)) 