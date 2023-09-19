
n=int(input("Nhập n: "))
s=int(0)
for i in range(1,n+1):
    if(i<=n):
        s=s + (i*(i+1)*(i+2))
print(int(s))