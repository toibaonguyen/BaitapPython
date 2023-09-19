
import math
x1=input("Nhap x1: ")
x1=int(x1)
x2=input("Nhap x2: ")
x2=int(x2)
x3=input("Nhap x3: ")
x3=int(x3)
y1=input("Nhap y1: ")
y1=int(y1)
y2=input("Nhap y2: ")
y2=int(y2)
y3=input("Nhap y3: ")
y3=int(y3)
print((x1,y1))
print((x2,y2))
print((x3,y3))
a=math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
b=math.sqrt(math.pow(x3-x2,2) + math.pow(y3-y2,2))
c=math.sqrt(math.pow(x3-x1,2) + math.pow(y3-y1,2))
p=(a + b + c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
s=int(s)
print(s)



