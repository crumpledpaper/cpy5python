import re

outfile = open('INVALID.DAT','a')

def check_alphabet(carplate):
    check_map = {0:'A',1:'Y',2:'U',3:'S',4:'P',5:'L',6:'J',7:'G',8:'D',9:'B',
                 10:'Z',11:'X',12:'T',13:'R',14:'M',15:'K',16:'H',17:'E',18:'C'}
    weights=[14,2,12,2,11,1]
    sum_products = 0
    sum_products += (ord(carplate[0])-ord('A')+1) * weights[0]
    sum_products += (ord(carplate[1])-ord('A')+1) * weights[1]
    for i in range(2,6):
        sum_products += int(carplate[i])* weights[i]
    remainder = sum_products % 19
    return check_map[remainder]
    
def validate():
    carplate = input('Enter carplate: ')
    if len(carplate)<5:
        return 'Invalid'
    carplate = carplate.upper()
    if carplate[2].isalpha():
        carplate = carplate[1:] #remove first letter
    if len(carplate)==5 or not carplate[5].isdigit():
        carplate = carplate[0:2] + '0' + carplate[2:] #append 0 to front of 3 numbers
    alphabet = check_alphabet(carplate)
    pattern = re.compile('^[A-Z]{2}[0-9]{4}$')
    if not pattern.match(carplate):
        pattern = re.compile('^[A-Z]{2}[0-9]{4}[A-Z]$')
        if not pattern.match(carplate):
            return 'Invalid'
        elif carplate[-1]!= alphabet:
            outfile.write(carplate+'\n')
            return ('Invalid ',alphabet)
        else:
            return ('Valid ',alphabet)
    else:
        return alphabet


outfile.close()
                
