#Filename: bmi_calculator.py
#Author: Bryan Ong
#Created: 2013/01/21
#Modified: 2013/01/21
#Description: Program to get user weight and height and
#calculate body mass index

#main
while True:
    try:
        height=float(input("Enter your height in metres\n"))  #prompt and get height
        break
    except ValueError:
        print("Error, please input a number\n")  #handles error if number is not input
while True:
    try:
        weight=float(input("Enter your weight in kilograms\n"))  #prompt and get weight
        break
    except ValueError:
        print("Error, please input a number\n")  #handles error if number is not input
bmi=weight/height**2  #calculate BMI

print("Your BMI is {0:.2f}".format(bmi))  #display result
