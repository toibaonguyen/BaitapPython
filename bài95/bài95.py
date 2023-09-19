import math
n=int(input("nhập n: "))
s=0
for i in range(n,0,-1):
    s=math.sqrt(i+s)
    
print(s)



