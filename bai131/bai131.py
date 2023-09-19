import math
xA=float(input("xA:"))
xB=float(input("xB:"))
xC=float(input("xC:"))
yC=float(input("yC:"))
yA=float(input("yA:"))
yB=float(input("yB:"))

A=math.sqrt((xB-xA)**2 + (yB-yA)**2)
B=math.sqrt((xC-xA)**2 + (yC-yA)**2)
C=math.sqrt((xC-xB)**2 + (yC-yB)**2)


if (A+B>C and A+C>B and B+C>A):
    print("La tam giac")
    
else:
    print("Ko la tam giac")


