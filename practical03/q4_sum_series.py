#Filename: q4_sum_series.py
#Author: Bryan Ong
#Created: 2013/02/18
#Modified: 2013/02/18
#Description: Summing series

def m_series(i):
    s=0
    print("i         m(i)")
    for n in range(1,i+1):
        s+=n/(n+1)
        print("{0:<10}{1:<.4f}".format(n,s))
