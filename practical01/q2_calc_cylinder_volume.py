#Filename: q2_calc_cylinder_volume.py
#Author: Bryan Ong
#Created: 2013/01/22
#Modified: 2013/01/22
#Description: Program to compute volume of a cylinder from radius and length

from math import pi
#main
radius = float(input("Enter radius: "))
length = float(input("Enter length: "))
area = pi * radius**2
volume = area * length
print("Volume: ",volume)
