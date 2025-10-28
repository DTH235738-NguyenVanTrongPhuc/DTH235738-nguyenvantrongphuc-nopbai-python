n = int(input("Nhập số phần tử n: "))
M = [float(input(f"M[{i}] = ")) for i in range(n)]

M.sort(reverse=True)
print("Dãy sau khi sắp xếp giảm dần:", M)
