#Filename: q5_upper_to_lower.py
#Author: Bryan Ong
#Created: 2013/01/22
#Modified: 2013/01/22
#Description: Program to convert an uppercase character to lowercase character

upper=input("Enter an uppercase letter: ")
lower=chr(ord(upper)-(ord("A")-ord("a")))
print(lower)
