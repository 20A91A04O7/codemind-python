s=input()
c=0
for i in s:
    if s.count(i)==1:
        c+=1
if c==len(s):
    print("Unique Number")
else:
    print("Not Unique Number")