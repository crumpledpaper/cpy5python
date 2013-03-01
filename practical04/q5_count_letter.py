#Filename: q5_count_letter.py
#Author: Bryan Ong
#Created: 2013/02/18
#Modified: 2013/02/18
#Description: Program to count number of letters in string

def count_letter(str,ch):
    if str=='':
        return 0
    else:
        return int(str[0]==ch) + count_letter(str[1:],ch)


