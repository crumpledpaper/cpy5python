#Filename: q08_top2_scores.py
#Author: Bryan Ong
#Created: 2013/01/30
#Modified: 2013/01/30
#Description: Program to find top 2 students

students_number=int(input("Enter the number of students: "))
first=["",0]
second=["",0]

for i in range(1,students_number+1):
    name = input("Enter name of student {0}: ".format(i))
    score = int(input("Enter score of student {0}: ".format(i)))
    if score>second[1]:
        if score>first[1]:
            first[0],first[1]= name,score
        else:
            second[0],second[1]= name,score
print (first[0],"has the highest score of",first[1])
print (second[0],"has the second-highest score of",second[1])
    
