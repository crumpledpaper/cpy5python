#Filename: q7_generate_payroll.py
#Author: Bryan Ong
#Created: 2013/01/22
#Modified: 2013/01/22
#Description: Program to generate payroll statement

#input
name=input("Enter name: ")
hours=int(input("Enter number of hours worked weekly: "))
rate=float(input("Enter hourly pay rate: "))
cpf=int(input("Enter CPF contribution rate(%): "))

#calculations
pay=hours * rate
contribution= pay * cpf / 100

#output
print("Payroll statement for " + name)
print("Number of hours worked in week:", hours)
print("Hourly pay rate: ${0:.2f}".format(rate))
print("Gross pay = ${0:.2f}".format(pay))
print("CPF contribution at",cpf,"% = ${0:.2f}".format(contribution))
