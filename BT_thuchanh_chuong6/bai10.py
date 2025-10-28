# Nhập ma trận A
row = int(input("Nhập số hàng: "))
col = int(input("Nhập số cột: "))

print("Nhập ma trận A:")
A = [[int(input(f"A[{i}][{j}] = ")) for j in range(col)] for i in range(row)]

print("Nhập ma trận B:")
B = [[int(input(f"B[{i}][{j}] = ")) for j in range(col)] for i in range(row)]

# Cộng hai ma trận
C = [[A[i][j] + B[i][j] for j in range(col)] for i in range(row)]
print("Tổng hai ma trận A + B:")
for rowC in C:
    print(rowC)

# Hàm hoán vị (chuyển vị)
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print("Ma trận hoán vị A^T:")
for r in transpose(A):
    print(r)

print("Ma trận hoán vị B^T:")
for r in transpose(B):
    print(r)
