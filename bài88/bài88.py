
n=int(input("n:"))
s=0
m=0
i=1
dau=+1
while i<=n:
    m=m+i
    s=s+dau/m
    i=i+1
    dau=-dau
print("s:",s)
