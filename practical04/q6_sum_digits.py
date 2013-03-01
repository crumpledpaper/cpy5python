#Filename: q6_sum_digits.py
#Author: Bryan Ong
#Created: 2013/02/18
#Modified: 2013/02/18
#Description: Program to sum digits of integer

def sum_digits(n):
    s=str(n)
    if s=='':
        return 0
    else:
        return int(s[0])+sum_digits(s[1:])
