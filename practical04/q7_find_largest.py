#Filename: q7_find_largest.py
#Author: Bryan Ong
#Created: 2013/02/18
#Modified: 2013/02/18
#Description: Program to find largest object in list

def find_largest(alist):
    if not alist:
        return 0
    largest = find_largest(alist[1:])
    if alist[0] > largest:
        return alist[0]
    else:
        return largest
