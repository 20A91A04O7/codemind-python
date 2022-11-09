n=int(input())
l=list(map(int,input().split()))
x=[]
for i in range(0,n):
    if i%2==0:
        x.append(l[i])
print(sum(x))
        
        
        
        