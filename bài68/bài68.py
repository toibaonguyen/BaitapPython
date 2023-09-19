n=int(input("nhập n: "))
s = 0
t = 1
i = 1
for i in range(1,n+1):
    if(i<=n):
        t=t*i
        s=s+t

print(s)

