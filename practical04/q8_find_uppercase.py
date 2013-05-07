#Filename: q8_find_uppercase.py
#Author: Bryan Ong
#Created: 2013/02/18
#Modified: 2013/02/18
#Description: Program to count number of uppercase letters in string

def find_num_uppercase(str):
    if not str:
        return 0
    elif ord('A')<=ord(str[0])<=ord('Z'):
        return 1 + find_num_uppercase(str[1:])
    else:
        return find_num_uppercase(str[1:])

print(find_num_uppercase(" HelloWorLd"))
