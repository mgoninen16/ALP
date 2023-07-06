'''
Reference Link
https://docs.google.com/document/d/1Lf221krWqB0vv5zSaQDvzBi6you6AuKdfn5x1TETh7Q/edit?usp=sharing
'''
'''
## Task Instructions - Beat The Zombie

This task requires you to combine lots of skills from earlier lessons. Don't be afraid to look at your old code, google ideas and have fun with the dialogue.  Good luck!

Write a program that simulates an encounter with a zombie in an RPG

1- Create a list of possible weapons.
2- In a variable called ‘zombieWeakness’ store the name of one of the weapons from the list.
3- Output messages telling the user that they have encountered a zombie and should prepare to fight.
4- Output the list of weapons to the user.  Ask if they want to type 1 to use one from the list or 2 to pick their own.  
  4.1- If they type 1 then they should input the weapon name - store it to a new variable. 
  4.2- If they type 2 they should input the weapon name - add it to the list and save it to a new variable.
5- If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  
  5.1- Otherwise output a message saying that they have lost.

'''

weapons = ["sword", "hands", "axe"]
zombieWeakness = weapons[0]

print("You have encountered a zombie and should prepare to fight.")
print("Here are your weapons: " + str(weapons))

wonFight = False
while not wonFight:
    choice = int(input("Enter '1' to choose a weapon from the list, or '2' to enter two of your own weapons: "))

    if choice == 1:
      listWeapon = input("Select a weapon from the list: ")
      if listWeapon == zombieWeakness:
        print("You have won the fight!")
        wonFight = True
      else:
        print("You have lost the fight. Try again.")
    elif choice == 2:
      ownWeapon1 = input("Please enter your first weapon choice: ")
      weapons.append(ownWeapon1)
      if ownWeapon1 == zombieWeakness:
        print("You have won the fight!")
        wonFight = True
      else:
        ownWeapon2 = input("Please enter your second weapon choice: ")
        weapons.append(ownWeapon2)
        if ownWeapon2 == zombieWeakness:
          print("You have won the fight!")
          wonFight = True
        else:
          print("You have lost the fight. Try again")
    else:
      print("Invalid input. Please enter '1' or '2'.")