

def count_letter(str,ch):
    if str=='':
        return 0
    else:
        return int(str[0]==ch) + count_letter(str[1:],ch)


