#to see the no of digit in number len does not work

#Data types

#1.strings
#print("Hello"[0])#subscript
#"123" #when it is in this code it is not treated as a number but as a string
#print("123"+"456")

#2.integer
#print(123+456)

#3.float
#print(3.14159)

#4.boolean
#True
#False

#----------
#changing integer into string or basically a number
# num_char=len(input("what is your name?"))
# new=str(num_char)
# print(type(new))
#float()
#print(70+float(100.5))

#A.
#35=3+5=8
# a=(input("enter any two digit number:"))
#print(int(a[0]) + int(a[1]))

# **->exponent
#eg 2**3=8

#Priority(PEMDAS)-> () ** * / + -

#B.
# height=input("enter your height in m:")
# weight=input("enter your weight in kg:")
# BMI=(float(weight))/(float(height) ** 2)
# print(BMI)

#print(round(8/3,2))
#print(8//3)#gives integer only

#without changing into integer or str you canuse f string
# score=0
# height=1.8
# isWinning=True
# print(f"Your score is {score} and height is {height} and is {isWinning}")

#
# age=input("what is your current age?")
# years=90*365
# month=90*12
# week=90*52
# new_years=years-(int(age)*365)
# new_month=month-(int(age)*12)
# new_weeks=week-(int(age)*52)
# print(f"You have {new_years} days, {new_month} months and{new_weeks} weeks")

print("Welcome to the tip calculator!")
total=float(input("Enter the total bill:"))
tip=float(input("What percentage tip would you like to give? 10, 12 or 15?"))
no=float(input("How many person to split the bill?"))
actual_tip=tip/100
actual_total=total+(total*actual_tip)
should_pay=actual_total/no
print(f"Each person should pay:{should_pay}")