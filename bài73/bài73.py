

x=int(input("x:"))
n=int(input("n:"))
s=0
t=1
m=0
i=1
while i<=n:
    t=t*x
    m=m+i
    s=s+t/m
    i=i+1
print("s:",s)
