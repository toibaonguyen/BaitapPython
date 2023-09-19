import math
xA = float(input("Nhap xA: "))
yA = float(input("Nhap yA: "))
xB = float(input("Nhap xB: "))
yB = float(input("Nhap yB: "))
xC = float(input("Nhap xC: "))
yC = float(input("Nhap yC: "))
xM = float(input("Nhap xM: "))
yM = float(input("Nhap yM: "))
sABC = math.fabs(xA * yB+ xB * yC + xC * yA - xB * yA - xC * yB * xA * yC) / 2
sMAB = math.fabs(xA * yB + xB * yM + xM * yA - xB * yA- xM * yB- xA * yM) / 2
sMBC = math.fabs(xM * yB+ xB * yC+ xC * yM - xB * yM - xC * yB - xM * yC) / 2
sMAC = math.fabs(xA * yM+ xM * yC+ xC * yA - xM * yA - xC * yM - xA * yC) / 2
s = sMAB + sMAC + sMBC
if(s == sABC):
    print("M trong")
else:
    print("M ngoai")
