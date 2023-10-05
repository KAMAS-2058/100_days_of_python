print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure")
input1 = input("You'\re at a crossroad. would you like to go left or right? ").lower()

if input1 == "left":
    input2 = input("There's a lake up ahead, with an island inside. You can wait for a boat or you can try to swim to it.").lower()
    if input2 == "wait":
      input3 = input("You arrive at the island unharmed thanks to a friendly fisherman! You see a house ahead with 3 doors. One red,another blue and a final one is yellow, which do you choose?").lower()
      if input3 == "red":
         print("you see the treasure before you! Congradulations! WINNAR!!!")
      elif input3 == "yellow":
         print("You enter the yellow room and immidiatly fall through a trap door! Game Over.")
      elif input3 == "blue":
         print("You open the blue door and water rushes out sweeping you out of the house and into the lake! A sturgeon gets you\
               Game Over.")
      else:
         print("Your willpower fails you and you can't bring yourself to open the door. you go home. Game Over")
    else:
       print("you were attacked by a sturgeon!")        
if input1 == "right":
  print("you fell into a hole and died! Game Over")