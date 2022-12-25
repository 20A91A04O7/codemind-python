n=int(input())
l=list(map(int,input().split()))
s=a=0
for i in range(0,n):
    if i%2==0:
        s+=int(l[i])
for j in range(0,n):
    if j%2!=0:
        a+=int(l[j])
if int(a-s)==0:
    print("YES")
else:print("NO")