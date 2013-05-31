def dec_to(dec_n, base):
    n = ''
    while dec_n != 0:
        remainder = dec_n % base
        if remainder >= 10:
            remainder = chr(remainder + 55)
        n = str(remainder) + n
        dec_n //= base
    return n

        
