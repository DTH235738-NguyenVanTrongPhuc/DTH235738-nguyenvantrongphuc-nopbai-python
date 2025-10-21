import math

print(" TÍNH ĐỘ DÀI ĐOẠN AB ")

# Nhập tọa độ 2 điểm
xA = float(input("Nhập hoành độ điểm A (xA): "))
yA = float(input("Nhập tung độ điểm A (yA): "))
xB = float(input("Nhập hoành độ điểm B (xB): "))
yB = float(input("Nhập tung độ điểm B (yB): "))

# Tính độ dài đoạn AB
AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

print(f"Độ dài đoạn AB = {AB:.3f}")
