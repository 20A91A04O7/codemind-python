n=int(input( ))
a=str(n**2)
b=str(n)
c=b[::-1]
d=int(c)
sq=str(d**2)
rev=sq[::-1]
if a==rev:
    print("True")
else:
    print("False")
