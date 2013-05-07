def linear_search(a,b):
    for i in range(len(a)):
        if a[i]==b:
            return i
    return -1


a=[4,2,5,3,1]
print(linear_search(a,2))
print(linear_search(a,0))
