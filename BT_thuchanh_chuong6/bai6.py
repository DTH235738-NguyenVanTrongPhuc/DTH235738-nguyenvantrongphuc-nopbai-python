import random

N = int(input("Nhập số lượng phần tử N: "))
lst = random.sample(range(0, 100), N)  # sinh N số ngẫu nhiên KHÔNG trùng nhau trong [0, 100)
print("Danh sách ngẫu nhiên không trùng:", lst)
