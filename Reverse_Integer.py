n=int(input())
s1=0
j=0
if n<0:
    j+=1
n=abs(n)
while n>0:
    r=n%10
    s1=s1*10+r
    n=n//10
if j==1:
    print(-s1)
else:
    print(s1)