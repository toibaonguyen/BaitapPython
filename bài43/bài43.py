



n=float(input("n:"))
s=0
i=1
while i<=n:
    s=s+(i/(i*(i+1)*(i+2)))
    i=i+1
print("s:",s)
