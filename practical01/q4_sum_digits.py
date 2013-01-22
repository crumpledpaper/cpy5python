#Filename: q4_sum_digits.py
#Author: Bryan Ong
#Created: 2013/01/22
#Modified: 2013/01/22
#Description: Program to sum all digits in an integer

n=int(input("Enter an integer:"))
digitsum = 0
while n!=0:
    digitsum += n % 10
    n //= 10
print("Digit sum =",digitsum)
