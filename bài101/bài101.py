
s=0
e=0.5
i=2
while e>= 10**(-6):
    e=1/i
    s=s+e
    i=i+1

print(s)
