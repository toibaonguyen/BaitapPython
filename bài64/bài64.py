
n=int(input("n:"))
lc=n%10
t=n
while t!=0:
    dv=t%10
    if dv>lc:
        lc=dv
    t=t//10
print("lc:",lc)
