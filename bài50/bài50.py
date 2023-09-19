n=int(input("Nhập n: "))
s=int(0)
for i in range(1,n+1):
    if(i<=n):
        if(n%i==0):
            s=s+i
            
    
print(int(s))
