import math

print(" TÍNH LOGₐ(X) ")

a = float(input("Nhập cơ số a: "))
x = float(input("Nhập số x: "))

if a > 0 and a != 1 and x > 0:
    loga_x = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {loga_x:.5f}")
else:
    print("❌ Lỗi: yêu cầu a > 0, a != 1, và x > 0")
