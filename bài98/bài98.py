n=int(input("nhập n: "))
s=0
for i in range(2,n+1,1):
    t=i+s
    s=t**(1/i)

print(s)
