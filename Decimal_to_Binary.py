n=int(input())
for i in range(n):
    a=int(input())
    b=str(bin(a))
    i=[]
    i.append(int(b[2:]))
    print(*i)