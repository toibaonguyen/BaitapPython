n = int(input("Nhập số nguyên dương n: "))

s = 0
for i in range(1, n):
    if n % i == 0:
       s+= i

if s == n:
    print(n, "là số hoàn thiện.")
else:
    print(n, "không là số hoàn thiện.")
    
