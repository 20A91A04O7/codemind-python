t=int(input())
for i in range(t):
    n=int(input())
    a=str(n)
    b=a[::-1]
    if a==b:
        print("True")
    else:
        print("False")