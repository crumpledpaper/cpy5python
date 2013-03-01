#Filename: q1_sum_series.py
#Author: Bryan Ong
#Created: 2013/02/18
#Modified: 2013/02/18
#Description: Program to sum harmonic series

def sum_series1(i):
    if i==1:
        return 1
    else:
        return 1/i+sum_series1(i-1)
