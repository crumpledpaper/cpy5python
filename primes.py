from math import sqrt
with open("PRIMES.dat","rb") as infile:
    infile.seek(-1024,2)
    last = int(infile.readlines()[-1])+2
with open("PRIMES.dat","a") as outfile:
    def is_prime(n):
        if n%2==0:
            return False
        check=3
        limit=sqrt(n)
        while check<=limit:
            if n%check==0:
                return False
            else:
                check+=2
        return True

    def prime_finder(n):
        while True:
            if is_prime(n):
                return str(n)+'\n'
            n+=1
    while True:
        last = prime_finder(last)
        outfile.write(last)
        last=int(last)+2
