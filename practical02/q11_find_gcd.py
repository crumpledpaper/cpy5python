#Filename: q11_find_gcd.py
#Author: Bryan Ong
#Created: 2013/01/30
#Modified: 2013/01/30
#Description: Program to compute greatest common divisor of two integers

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

if a<b:
    a,b=b,a

#while loop definition
while a!=0 and b!=0:
    a,b=b,a%b

print("The GCD is",a)


#recursive definition
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

