#Filename: q12_find_factors.py
#Author: Bryan Ong
#Created: 2013/01/30
#Modified: 2013/01/30
#Description: Program to display prime factors of number

n=int(input("Enter number: "))
i=2

while n!=1:
    if n%i==0:
        n/=i
        if n!=1:
            print(i, end=', ')
            continue
        else:
            print(i)
    i+=1
