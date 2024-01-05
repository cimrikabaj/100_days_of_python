#randomization and python list

import random
# import my_module
# random_integer=random.randint(1,10)
# print(random_integer)
# print(my_module)

# random_float=random.random()#0.0 to 0.999999
# print(random_float)

# random_float=random.random()*5
# print(random_float)

# random_side=random.randint(0,1)
# if random_side==1:
#     print("Heads")
# else:
#     print("Tails")

#list=[]=>can store any datatype,have an order depends on the items on the list
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[2])
# print(states_of_america[-2])
# states_of_america[0]="Ohio"
# print(states_of_america)

# name_string=input("Enter everybody's name separated by a comma.")
# name=name_string.split(",")
# print((name))#returns the result in a list form

# sentence="Micheal is going to buy the meal today!"
# a=sentence.split(" ")
# print(a)

#random name generator
# names=input("enter random amount of name separated by comma:")
# n=names.split(",")
# #print(len(n))
# no=len(n)
# a=random.randint(0,no-1)
# print(n[a])

# or
# a=random.choice(n)
# print(a)

# dirty_dozen=["strawberries","spinach","kale","nectarines","apples","grapes","peaches","cherries","pears","tomatoes","celery","potatoes"]
# fruits=["strawberries","nectarines","apples","grapes","peaches","cherries","pears"]
# vegetables=["spinach","kale","tomatoes","celery","potatoes"]
# dirty_dozen=[fruits,vegetables]
# print(dirty_dozen)

# row1=["⬜","⬜","⬜"]
# row2=["⬜","⬜","⬜"]
# row3=["⬜","⬜","⬜"]
# map=[row1,row2,row3]
# print(f"{row1}\n{row1}\n{row3}")
# position=input("where do you want to put the treasure?")
# horizontal=int(position[0])
# vertical=int(position[1])
# selected_row=map[vertical-1]
# selected_row[horizontal-1]="X"
# print(f"{row1}\n{row1}\n{row3}")
#or
# map[vertical-1][horizontal-1]="X"


#rock,paper,scissor
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!") 
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")


