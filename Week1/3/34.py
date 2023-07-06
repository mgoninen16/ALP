'''
Chat-Bot Challenge

Lots of websites use chat bots to interact with their customers.  These chat bots are often very sophisticated and use AI to learn and adapt to the user.  Our chat bot is going to be a bit simpler.

The chat bot should work like this:

1.Ask the user their name and store it in a variable.
2. Greet the user by name.
3. Ask the user three(or four) questions about themselves and store their responses in three(or four) different suitably named variables.
4. Respond to each of the questions one by one, using the 5. user’s name in the response.
5. Output a summary of all of the user’s answers in a single sentence.

'''

name = input("What's your name?")
print("Hello, " + name)
print()
homeTown = input("What's your hometown named?")
print(homeTown + " sounds like a lovely place, " + name + "!")
print()
favTVshow = input("What is your favorite TV show?")
print(favTVshow + " is a great show! You've got great taste in TV, " + name + ".")
print()
hobby = input("What is your favorite hobby?")
print(hobby + " sounds so fun and interesting, " + name + "!")
print()
season = input("What is your favorite season?")
print("Wow, " + name + " I also love " + season + "!")
print()
print("It was great talking to you, " + name + ". Your hometown is named " + homeTown + ", you like to watch " + favTVshow + " on TV, your favorite hobby is " + hobby + ", and you love " + season + ". Talk to you later!")