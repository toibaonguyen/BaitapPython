
x=int(input("x:"))
n=int(input("n:"))
s=-1
t=1
m=1
i=2
dau=+1
while i<=2*n:
    t=t*x*x
    m=m*i*(i-1)
    s=s+(dau*t)/m
    i=i+2
    dau=-dau
print("s:",s)
