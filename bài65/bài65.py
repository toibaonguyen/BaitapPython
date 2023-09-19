
n = int(input("Nhập số nguyên dương n: "))

# Chuyển số nguyên n thành chuỗi ký tự để dễ xử lý
str_n = str(n)

# Gán chữ số đầu tiên là chữ số nhỏ nhất
min_digit = int(str_n[0])

# Duyệt qua các chữ số còn lại trong chuỗi
for i in range(1, len(str_n)):
    digit = int(str_n[i])
    if digit < min_digit:
        min_digit = digit

print("Chữ số nhỏ nhất của số n là:", min_digit)


