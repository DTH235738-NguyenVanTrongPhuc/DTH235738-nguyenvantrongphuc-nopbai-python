# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử của mảng: "))

# Khởi tạo mảng rỗng
arr = []

# Nhập từng phần tử
for i in range(n):
    while True:
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        if x >= 0:
            arr.append(x)
            break
        else:
            print("Vui lòng nhập số tự nhiên (>= 0)")

# In ra mảng sau khi nhập
print("Mảng bạn đã nhập là:", arr)
print("các số lẻ là :", [x for x in arr if x % 2 != 0])
print ("tong cac so le la :", sum(x for x in arr if x % 2 != 0))
print("các số chẵn là :", [x for x in arr if x % 2 == 0])
print ("tong cac so chan la :", sum(x for x in arr if x % 2 == 0))
print("các số nguyên tố là :", [x for x in arr if all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1])
print("khong phai so nguyen to la :", [x for x in arr if any(x % i == 0 for i in range(2, int(x**0.5) + 1)) or x < 2])
