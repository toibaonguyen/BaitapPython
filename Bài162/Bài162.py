n = int(input("Nhap n: "))
flag = 1
t = n
while(t >= 10):
    dv = t % 10
    hc = (t/10) % 10
    if(hc < dv):
        flag = 0
    t = t // 10
if(flag == 1):
    print("Giam")
else:
    print("Khong giam")
