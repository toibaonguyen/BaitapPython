
n=int(input("n:"))
s=0
t=1
i=1
while i<=n:
    t=t*i
    s=s+i*t
    i=i+1
print("s:",s)
