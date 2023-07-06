grade = int(input("Please input your test score (between 1 and 100)."))
print()

if grade < 0:
  fail = "N"
elif 0 <= grade < 40:
  fail = "Y"
elif grade >= 40:
  fail = "N"

if fail != "N":
  print("Retake Required")
  print("Grade: U")
elif 40 <= grade <= 68:
  print("Pass \nGrade: C")
elif 69 <= grade <= 79:
  print("Pass \nGrade: B")
elif 80 <= grade <= 100:
  print("Pass \nGrade: A")
else:
  print("Please try again; enter a score between 1 and 100.")