#Filename: q8_convert_milliseconds.py
#Author: Bryan Ong
#Created: 2013/02/19
#Modified: 2013/02/19
#Description: Converting milliseconds to hours, minutes, and seconds

def convert_ms(n):
    n//=1000  #Convert to seconds
    return "{0}:{1}:{2}".format(n//3600,n//60%60,n%3600%60)
