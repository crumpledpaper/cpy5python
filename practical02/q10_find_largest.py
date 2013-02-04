#Filename: q10_find_largest.py
#Author: Bryan Ong
#Created: 2013/01/30
#Modified: 2013/01/30
#Description: Program to find smallest n such that n^3 < 12000

n=0
while pow(n,3)<12000:
    n+=1
print(n-1)
