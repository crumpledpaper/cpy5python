#Filename: q5_compute_series.py
#Author: Bryan Ong
#Created: 2013/02/18
#Modified: 2013/02/18
#Description: Computing series

def m_series(i):
    s=4
    for n in range(1,2*i+2,2):
        if n%4==1:
            s-=1/n
        else:
            s+=1/n
        print("{0:<5}{1}".format(n,s))
