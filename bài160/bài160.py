
n=int(input("n:"))
dt=n
while (dt>=10):
    dt=dt//10
    
dem=0
t=n
while t!=0:
    dv=t%10
    if(dv==dt):
        dem=dem+1
    t=t//10
    
print("dem:",dem)