
x=int(input("nhập x: "))
n=int(input("nhập n: "))
s=1-x
t=x
m=1
dau=+1
for i in range(3,2*n+1,2):
    t=t*x*x
    m=m*i*(i-1)
    s=s+dau*t/m
    dau=-dau

print(s)