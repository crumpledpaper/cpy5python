#Filename: q2_display_pattern.py
#Author: Bryan Ong
#Created: 2013/02/15
#Modified: 2013/02/15
#Description: Displaying patterns

def display_pattern(n):
    length_n=len(str(n))
    for i in range(1,n+1):
        length_i=len(str(i))
        for l in range(length_n):
            print(" "*(l*(n-i)),end="")
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
display_pattern(13)
