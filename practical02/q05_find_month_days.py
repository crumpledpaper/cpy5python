#Filename: q05_find_month_days.py
#Author: Bryan Ong
#Created: 2013/01/29
#Modified: 2013/01/29
#Description: Program to find the number of days in a month

month=int(input("Enter month: "))-1
year=int(input("Enter year: "))
month_names=["January","February","March","April","May","June",\
            "July","August","September","October","November","December"]
days=[31,28,31,30,31,30,31,31,30,31,30,31]

if month!=1:
    print(month_names[month],year,"has",days[month],"days")
else:
    if year%400==0 or year%4==0 and year%100!=0:
        print(month_names[month],year,"has",days[month]+1,"days")
    else:
        print(month_names[month],year,"has",days[month],"days")
