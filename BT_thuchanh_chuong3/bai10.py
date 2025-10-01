n=int(input("nhap n: "))
x=int(input("nhap x: "))
s=0
for i in range(1,n+1):
    tu=x**i
    mau=1
for j in range(1,i+1):
    mau=mau*j
s+=(tu/mau)
print("ket qua la ",s)