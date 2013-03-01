#Filename: q6_determine_prime.py
#Author: Bryan Ong
#Created: 2013/02/19
#Modified: 2013/02/19
#Description: Check primality and display primes

from math import sqrt
try:
    infile = open("PRIME.IN.txt","r")
    outfile= open("PRIME.OUT.txt","a")
    n = int(infile.readline())
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

    def prime_finder(n):
        i=2
        count=0
        while count<n:
            if is_prime(i):
                count+=1
            if count==n:
                return i
            i+=1
    outfile.write(str(prime_finder(n)))
    infile.close()
    outfile.close()
except IOError:
    print("File not found")

