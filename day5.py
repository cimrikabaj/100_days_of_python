##For Loops, Range and Code Blocks

#syntax: for item in list_of_item:

# fruits=["apple","mango","orange","guava"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit+"pie")

#finding the average height of the students
# students_heights=input("Input a list of student's height:").split()
# for n in range(0, len(students_heights)):
#     students_heights[n]=int(students_heights[n])
# print(students_heights)
# total_height=0
# n=0
# for height in students_heights:
#     n+=1
#     print(n)
#     total_height+=height
# avg_height=round(total_height/n)

# print("The average height is", avg_height)

#or use len() and sum()

#finding the heighest score
# student_scores=input("Input a list of students score:").split()
# for n in range(0,len(student_scores)):
#     student_scores[n]=int(student_scores[n])
# print(student_scores)
# #print(max(student_scores))
# #print(min(student_scores))
# heighest_score=0
# for scores in student_scores:
#     if scores>heighest_score:
#         heighest_score=scores
# print(f"the highest score in the class is:{heighest_score}")

#for loop with range:
# for number in range(1,10,2):
#     print(number)

# total=0
# for number in range(1,101):
#     total += number
# print(total)

#adding even number exercise
# sum=0
# for i in range(0,101,2):
#     sum = sum +i
# print(sum)

#or
# for i in range(1,101):
#     if i % 2==0:
#         sum += i
# print(sum)

#FizzBuzz
#a game where when the number is divisible by 3 then instead of printing the number it should print"Fizz" and when it is divisible by 5 then it should print "buzz" anf if both then it should print "fizzbuzz"
# for i in range(1,50):
#     if i % 3==0:
#         print("Fizz")
#     elif i % 5==0:
#         print("Buzz")
#     elif i%3==0 & i%5==0:
#         print("Fizz Buzz")
#     else:
#         print(i)


#pypassword generator
import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
        'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G',
        'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!', '#', '$', '%', '&', '(', ')','*','+']
print("Welcome to the PyPassword Generator!!\n")
no_of_letter=int(input("How many letters would you like in your password?\n"))
no_of_symbol=int(input("How many symbols would you like?\n"))
no_of_digit=int(input("How many numbers would you like?\n"))

#eazy level=fghf^123
# password=""
# for char in range(1,no_of_letter+1):
#     letterrandom= random.choice(letter)
#     password+=letterrandom
# for char in range(1,no_of_symbol+1):
#     letterrandom= random.choice(symbols)
#     password+=letterrandom
# for char in range(1,no_of_digit+1):
#     password+=random.choice(numbers)
# print(password)
# print(f"Here is your password:{password}")

#hard level=g^2jk8&
password=""
password_list=[]
for char in range(1,no_of_letter+1):
    password_list.append(random.choice(letter))
for char in range(1,no_of_symbol+1):
    password_list.append(random.choice(symbols))
for char in range(1,no_of_digit+1):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)

for i in password_list:
    password+=i
print(f"Here is your password:{password}")