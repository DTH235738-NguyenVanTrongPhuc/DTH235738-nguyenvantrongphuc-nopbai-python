import math
n=int(input('nhap so n ="'))
x=int(input('nhap so x ="'))
for i in range(1,n+1):
    s=x*i/math.factorial(i)
    print(f"ket qua cua {x}^{i}/{i}! la: ",s)
    s+=s
print("tong ket qua la: ",s)