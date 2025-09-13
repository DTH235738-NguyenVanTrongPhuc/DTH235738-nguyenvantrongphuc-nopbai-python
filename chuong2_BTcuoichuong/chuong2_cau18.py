def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input("Nhập số n: "))
count = 0

for i in range(2, n + 1):
    if n % i == 0 and is_prime(i):
        count += 1

print("Số lượng ước số nguyên tố khác nhau của", n, "là:", count)
#tinh tong
s=0
for i in range (n):
   s=s+i
print("tong cac so thuc la:",s)    
#tinh tong 12+22+32..n
t=0
for i in range (12,n,10):
    t+=i
print("tong la: ",t)    


