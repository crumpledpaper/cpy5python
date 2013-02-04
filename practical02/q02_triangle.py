#Filename: q02_triangle.py
#Author: Bryan Ong
#Created: 2013/01/29
#Modified: 2013/01/29
#Description: Program to validate triangle and compute perimeter

a=float(input("Enter side 1: "))
b=float(input("Enter side 2: "))
c=float(input("Enter side 3: "))

if a+b>c and b+c>a and a+c>b:
    print("Perimeter =",a+b+c)
else:
    print("Invalid triangle!")
