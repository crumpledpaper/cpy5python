#Filename: q4_print_reverse.py
#Author: Bryan Ong
#Created: 2013/02/18
#Modified: 2013/02/18
#Description: Program to reverse integer

def reverse_int(n):
    s=str(n)
    if not s:
        return s
    else:
        return s[-1]+reverse_int(s[:-1])
