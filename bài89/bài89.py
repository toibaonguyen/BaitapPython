
x=int(input("Nhap x: "))
n=int(input("Nhap n: "))
s=0
t=1
m=0
dau=-1
for i in range(1,n+1):
    t=t*x
    m=m+i
    s=s+(dau*t/m)
    dau=-dau

print(s)

    