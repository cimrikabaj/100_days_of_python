# import pandas as pd
# import numpy as np
# X=np.array([[1,0,1],[2,2,2]]) 
# out=X[0,1:3]
# print(out)
# X=np.array([[1,0],[0,1]])
# Y=np.array([[2,2],[2,2]])
# Z=np.dot(X,Y)
# print(Z)
# "1:2,3:4".split(':')
# A=['1','2','3']
# for a in A:
#     print(2*a)


#odd or even
# n=int(input("enter any number:"))
# if n % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")


#bmi calculator
# height=float(input("enter your height in meter:"))
# weight=float(input("enter your weight in kilogram:"))
# BMI=(float(weight))/(float(height) ** 2)
# print(f"Your BMI is {BMI}.")
# if BMI < 18.5:
#     print("You are underweight.")
# elif BMI<25:
#     print("You have normal weight.")
# elif BMI>30:
#     print("you are overwight.")
# elif BMI>35:
#     print("You are obese.")
# else:
#     print("you are clinically obese.")


#leap year
# year=int(input("Enter the year you want to check."))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("This is a leap year!")
#         else:
#             print("this is not leap year!")
#     else:
#         print("This is a leap year!")
# else:
#     print("this is not leap year!")


#task
# small pizza:$15
# medium pizza:$20
# large pizza:$25
# pepperoni for small pizza:+$2
# pepperoni for medium or large pizza:+$3
# extra chesse:+$1

# print("welcome to pizza deliveries")
# size=input("what size of pizza do you want?S,M,L")
# add_pepperoni=input("do you want pepperoni?Y or N")
# extra_cheese=input("do you want extra chesse?Y or N")
# bill=0
# if size=="S":
#     bill+=15
# elif size=="M":
#     bill+=20
# else:
#     bill+=25
# if add_pepperoni=="Y":
#     if size=="S":
#         bill+=2
#     else:
#         bill+=3
# if extra_cheese=="Y":
#     bill+=1
# print(f"You final bill is ${bill}.")

#
# name1=input("enter your name.")
# name2=input("enter their name.")
# combined_string=name1+name2
# name=combined_string.lower()
# true=name.count("t")+name.count("r")+name.count("u")+name.count("e")
# love=name.count("l")+name.count("o")+name.count("v")+name.count("e")
# total=str(true)+str(love)
# print(total)


#treasure island
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
print("Welcome to Treasure Island!!\n")
print("Your mission is to find the treasure.So,lets us begin.")
first_input=input("You're at a cross road. Where do you want to go? Type 'left' or 'right'.")
if first_input=="right":
    print("You have fallen into a hole. Game over!!")
else:
    second_input=input("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat or type 'swim' to swim across.")
    if second_input=="swim":
        print("Attacked by trout. Game over!!")
    else:
        third_input=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        if third_input=="red":
            print("Burned by fire. Game over!!")
        elif third_input=="blue":
            print("Eaten by beats. Game Over!!")
        elif third_input=="yellow":
            print("You Win!!")
        else:
            print("Game Over!!")