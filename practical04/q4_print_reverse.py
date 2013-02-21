

def reverse_int(n):
    s=str(n)
    if not s:
        return s
    else:
        return s[-1]+reverse_int(s[:-1])
