
n=int(input("Nhập n: "))
s=int(0)
for i in range(1,n+1):
    if(i<=n):
        s=s + (1/(i*(i+1)*(i+2)*(i+3)))
print(float(round(s,2)))