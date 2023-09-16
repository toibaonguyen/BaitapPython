

n=int(input("n:"))
dem=0
t=n
while t!=0:
    dv=t%10
    if dv%2!=0:
        dem=int(dem)+1
    t=int(t/10)
print("dem:",dem)
