#Filename: q2_display_pattern.py
#Author: Bryan Ong
#Created: 2013/02/15
#Modified: 2013/02/15
#Description: Displaying patterns

def display_pattern(n):
    length_n=len(str(n))-1
    length_i=0
    for i in range(1,n+1):
        length_i+=len(str(i))-1
        print(" "*(length_n-length_i+2*n-2*i),end="")
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
