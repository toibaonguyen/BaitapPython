n = int(input("Nhap n: "))
ic = n % 10
dem = 0
t = n
while(t != 0):
    dv = t % 10
    if (dv < ic):
        ic = dv
    t = t // 10
t = n
while(t != 0):
    dv = t % 10
    if(dv == ic):
        dem += 1
    t = t // 10
print("So luong chu so nho nhat:", dem)    
