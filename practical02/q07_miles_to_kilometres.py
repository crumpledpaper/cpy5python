#Filename: q07_miles_to_kilometres.py
#Author: Bryan Ong
#Created: 2013/01/29
#Modified: 2013/01/29
#Description: Program to display conversion table from kilometres to miles

print("Miles Kilometers Kilometres Miles")
for n in range(10):
    print("{0:<6}{1:<11.3f}{2:<11}{3:.3f}".format\
          (n+1,(n+1)*1.609,20+n*5,(20+n*5)/1.609))
