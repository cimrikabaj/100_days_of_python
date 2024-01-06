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

#no7