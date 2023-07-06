'''
Task - Which Room?
----------------------

Write a program that asks the user for their name and which subject they are studying.
The program should output a message telling the student by name which room to go to for that class (make up the room numbers if you need to).  You should include at least 3 subjects and have a message such as 'I don't know which room that class is in' for any you don't include.
 Example - an input of 'Ben' and 'Computing' might get an output of 'Hi Ben, go to room 401 for Computing'


You may use any method taught in class that is appropriate for this task. There is room for interpretation.

'''
#Start coding below

name = input("What is your name? \n")
subject = input("\nHello, what subject are you studying? \n")

if subject.lower() == "math" or subject.lower() == "maths" or subject.lower() == "mathmatics":
  print("\n" + name + ", math is in room 213.")
elif subject.lower() == "english":
  print("\n" + name + ", english is in room 716.")
elif subject.lower() == "science":
  print("\n" + name + ", science is in room 492.")
elif subject.lower() == "spanish":
  print("\n" + name + ", spanish is in room 381.")
elif subject.lower() == "history" or subject.lower() == "social studies" :
  print("\n" + name + ", social studies is in room 577.")
elif subject.lower() == "pe" or subject.lower() == "gym" or subject.lower() == "physical education":
  print("\n" + name + ", physical education is in room 183.")
elif subject.lower() == "computer science" or subject.lower() == "programming" or subject.lower == "computing":
  print("\n" + name + ", computer science is in room 903.")
else:
  print("I don't know which room that class is in.")