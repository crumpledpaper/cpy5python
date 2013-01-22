#Filename: q1_fahrenheit_to_celsius.py
#Author: Bryan Ong
#Created: 2013/01/22
#Modified: 2013/01/22
#Description: Program to convert fahrenheit to celsius

fahrenheit=float(input("Enter temperature in F: "))
celsius = (5/9) * (fahrenheit - 32)
print(fahrenheit,"F = {0:.1f}".format(celsius),"C")
