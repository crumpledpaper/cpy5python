

def find_num_uppercase(str):
    if not str:
        return 0
    elif ord('A')<=ord(str[0])<=ord('Z'):
        return 1 + find_num_uppercase(str[1:])
    else:
        return find_num_uppercase(str[1:])
