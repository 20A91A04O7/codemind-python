n=int(input())
b=len(str(n))
c=n*n
d=c%(pow(10,b))
if n==d:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    