
n=int(input("Nhap n: "))
s=float(0)
for i in range(1,n+1):
    if(i<=n):
        s=s + 1/(i*(i+1))

print("{:.2f}".format(s))

        