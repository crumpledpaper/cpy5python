#Filename: q3_find_gcd.py
#Author: Bryan Ong
#Created: 2013/02/18
#Modified: 2013/02/18
#Description: Program to compute greatest common divisor of two integers

def gcd(a,b):
    if a<b:
        a,b=b,a
    while a!=0 and b!=0:
        a,b=b,a%b
    return a
