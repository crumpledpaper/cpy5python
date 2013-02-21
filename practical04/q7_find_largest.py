

def find_largest(alist):
    if not alist:
        return 0
    largest = find_largest(alist[1:])
    if alist[0] > largest:
        return alist[0]
    else:
        return largest
