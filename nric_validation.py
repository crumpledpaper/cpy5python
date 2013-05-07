import re

def check_alphabet(nric):
    if nric[0] in ['S','s','T','t']:
        check_map = {0:'J',1:'Z',2:'I',3:'H',4:'G',5:'F',6:'E',7:'D',8:'C',
                     9:'B',10:'A'}
    if nric[0] in ['F','f','G','g']:
        check_map = {0:'X',1:'W',2:'U',3:'T',4:'R',5:'Q',6:'P',7:'N',8:'M',
                     9:'L',10:'K'}
    weights=[2,7,6,5,4,3,2]
    sum_products = 0
    if nric[0] in ['T','t','G','g']:
        sum_products = 4
    for i in range(7):
        sum_products += int(nric[i+1]) * weights[i]
    remainder = sum_products % 11
    return check_map[remainder]

def validate(nric):
    pattern = re.compile("^[sStTfFgG][0-9]{7}[a-zA-Z]$")
    if not pattern.match(nric):
        return False
    elif nric[-1] != check_alphabet(nric):
        return False
    else:
        return True
