import math
a = input("nhap chuoi chu so:")

def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for c in a:
    if c.isdigit():  # kiem tra c co phai chu so khong
        print(c)
        if int(c) % 2 == 0:
            print("la so chan")
        if int(c) < 0:
            print("la so am")
        if snt(int(c)):
            print("la so nguyen to")

# Tính giá trị trung bình các chữ số
ds = [int(d) for d in a if d.isdigit()]
if ds:
    print("gia tri trung binh la :", sum(ds) / len(ds))
else:
    print("khong co chu so trong chuoi")