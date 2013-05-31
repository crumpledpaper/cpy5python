def checksum(postal_code):
    #each RM4SCC code is 1-6 in binary so step 1-3 can be ignored
    upper = 0
    lower = 0
    for i in postal_code:
        upper += int(i)//6 + 1
        lower += (int(i)+1)%6
    ref = ((upper-1)%6)*6 + (lower-1)%6 #multiply the row reference by 6 to convert the 2-dimensional array
    if ref<10: #if checksum is number(0-9)
        return str(ref)
    return chr(ref+55) #A is 10, B is 11...

#main
postal_code = 0
while postal_code != '-1':
    postal_code = input('Enter Postal Code (Enter -1 to quit): ')
    if postal_code == '-1':
        break
    if not postal_code[:-1].isdigit():
        print('Please enter numbers only')
        continue
    if len(postal_code)!=7:
        print('Postal code must be 7-digits')
        continue
    checkchar = checksum(postal_code[:-1])
    if checkchar != postal_code[-1] and checkchar != postal_code[-1].upper():
        print('Invalid. Expected checksum character is',checkchar)
        continue
    else:
        print('OK')
