'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",] #This is a list. The list is named "Sentence". The list has 7 items.
print(Sentence) #This print function will print the entire "Sentence" list, every item
print(Sentence[1]) #Since lists use 0 indexing (starting to count from 0 rather than 1), this will print the 2nd item in the list "Look" 
Sentence.append("life") #The .append method will at an item (in this case, the string "life) onto the end of list
Sentence[4] = "sunny" #This finds the 4th index in "Sentence" list and changes it from "bright" to "sunny"
print(Sentence[4]) #This indexes the 4th item of the list and prints the item.
print(Sentence[0] + " " + Sentence[3]) #this prints the 0 index item, plus a space, plus the 3 index item to the console
print(Sentence) #This prints the entire list with the changed item and appended item.