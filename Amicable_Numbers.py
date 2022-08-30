n=int(input())
m=int(input())
s=0
x=0
for i in range(1,n):
    c=n%i
    if c==0:
        s+=i
for j in range(1,m):
    c1=m%j
    if c1==0:
        x+=j
if n==x and m==s:
    print("Amicable")
else:
    print("Not Amicable")
        
        
        
        