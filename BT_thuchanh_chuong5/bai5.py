# Nhập vào 1 chuỗi
s = input("Nhập vào chuỗi: ")

# Khởi tạo biến đếm
hoa = thuong = so = dacbiet = 0

# Duyệt từng ký tự trong chuỗi
for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1
    elif ch.isdigit():
        so += 1
    else:
        dacbiet += 1

# Xuất kết quả
print("-" * 30)
print("Số chữ IN HOA: ", hoa)
print("Số chữ in thường: ", thuong)
print("Số chữ là chữ số: ", so)
print("Số ký tự đặc biệt: ", dacbiet)
print("Tổng số ký tự: ", len(s))
