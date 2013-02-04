#Filename: q04_determine_leap_year.py
#Author: Bryan Ong
#Created: 2013/01/29
#Modified: 2013/01/29
#Description: Program to determine if year is leap year

year=int(input("Enter year: "))

if year%400==0:
    print("Leap")
elif year%100==0:
    print("Non-Leap")
elif year%4==0:
    print("Leap")
else:
    print("Non-Leap")
