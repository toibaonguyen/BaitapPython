n=int(input("n:"))
at=1
bt=1
i=2
while i<=n:
    ahh=3*bt+2*at
    bhh=at+3*bt
    i=i+1
    at=ahh
    bt=bhh
print("ahh:",ahh)
print("bhh:",bhh)
