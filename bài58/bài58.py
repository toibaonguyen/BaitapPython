

n=int(input("n:"))
s=0
t=n
while t!=0:
    dv=t%10
    s=s+dv
    t=t/10
print("dem:",s)
