import datetime
import re

nric_pattern = re.compile("[^[sS][0-9]{7}[a-zA-Z]$]")
nric = input('Enter NRIC: ')
while not nric_pattern.match(nric):
    print("Invalid NRIC")
    nric = input("Enter NRIC: ")
name_pattern = re.compile("[1-30]")
name = input('Enter name: ')
while not name_pattern.match(name):
    name = input("Name must be 1-30 characters \nEnter name:")
cla = input('Enter class: ')
gender = input('Enter gender: ')
dob = input('Enter date of birth(DD-MM-YYYY): ')
weight = input('Enter weight(kg): ')
height = input('Enter height(metres): ')

