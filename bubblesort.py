def bubblesort(l):
    issort=1
    while issort<len(l):
        issort=1
        for n in range(len(l)):
            if n!=0:
                if l[n-1]>l[n]:
                    l[n-1],l[n]=l[n],l[n-1]
                    print(l)
                else:
                    issort+=1

