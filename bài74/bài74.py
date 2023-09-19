import math
x=int(input("nhập x: "))
n=int(input("nhập n: "))
s = 0
t=1
m=1 

for i in range(1,n+1):
    if(i<=n):
        t=t*x
        m=m*i
        s=s+t/m
        

print(s)    
