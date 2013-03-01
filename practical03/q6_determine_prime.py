#Filename: q6_determine_prime.py
#Author: Bryan Ong
#Created: 2013/02/19
#Modified: 2013/02/19
#Description: Check primality and display primes

from math import sqrt



def is_prime(n):
    if n==1:
        return False
    check=2
    limit=sqrt(n)
    while check<=limit:
        if n%check==0:
            return False
        else:
            check+=1
    return True

i=2
count=0
while count<1000:
    if is_prime(i):
        print("{0:<5}".format(i),end="")
        count+=1
        if count%10==0:
            print()
    i+=1
