#Filename: q2_sum_series2.py
#Author: Bryan Ong
#Created: 2013/02/18
#Modified: 2013/02/18
#Description: Program to sum series

def sum_series2(i):
    if i==1:
        return 1/3
    else:
        return i/(2*i+1)+sum_series2(i-1)
