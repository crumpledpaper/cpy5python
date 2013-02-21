

def sum_digits(n):
    s=str(n)
    if s=='':
        return 0
    else:
        return int(s[0])+sum_digits(s[1:])
