def check_parity(binary_pattern):
    p = binary_pattern
    x = len(p[0])
    y = len(p)
    parity = (int(p[0][0])+1)%2
    for i in range(y):
        s = 0
        for j in p[i]:
            s += int(j)
        if s%2 != parity:
            corrupt_y = i
            break
    for i in range(x):
        s = 0
        for j in p:
            s += int(j[i])
        if s%2 != parity:
            corrupt_x = i
            break
    return(corrupt_x, corrupt_y)

stream = '''00000010
00000100
10000101
00000111
10010011
10000101
00000001
10000101
11111001'''.split()
pos = check_parity(stream)
stream[pos[1]] = stream[pos[1]][:pos[0]]+str((int(stream[pos[1]][pos[0]])+1)%2)+stream[pos[1]][pos[0]+1:]

octal_number = ''.join([str(int(i[1:],2)) for i in stream[:-1]])
print(octal_number)

def oct_to_dec(oct_num):
    length = len(oct_num)
    dec_num = 0
    for i in range(length):
        dec_num += (int(oct_num[i]) * int((length-i-1)**8))
    return dec_num

