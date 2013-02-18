#Filename: q3_find_gcd.py
#Author: Bryan Ong
#Created: 2013/02/18
#Modified: 2013/02/18
#Description: Program to compute greatest common divisor of two integers

def gcd(x,y):
    if x<y:
        x,y=y,x
    if y==0:
        return x
    else:
        return gcd(y,x%y)
