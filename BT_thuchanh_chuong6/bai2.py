import random

# 1. Khởi tạo ngẫu nhiên n phần tử cho list
n = int(input("Nhập số phần tử n: "))
lst = [random.randint(0, 9) for _ in range(n)]  # sinh ngẫu nhiên số từ 0–9
print("Danh sách ban đầu:", lst)

# 2. Nhập k, xóa tất cả phần tử có giá trị k
k = int(input("Nhập giá trị k cần xóa: "))
lst = [x for x in lst if x != k]
print("Danh sách sau khi xóa tất cả phần tử =", k, ":", lst)

# 3. Kiểm tra list có đối xứng (palindrome) hay không
if lst == lst[::-1]:
    print("Danh sách đối xứng.")
else:
    print("Danh sách không đối xứng.")
