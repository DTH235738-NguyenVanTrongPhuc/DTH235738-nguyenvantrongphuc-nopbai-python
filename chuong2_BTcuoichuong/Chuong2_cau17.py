n=int(input("nhap so nguyen n "))
# Tinh tong 1+2+....2n

t=0
for i in range (1,n+1):
    t+=i
print("tong cac so la: ",t)
#tinh tong cac so tu nhien <n và lá số lẻs=0;
l=0
for i in range(1,n):
    if i%2 !=0:
        l+=i
print("tong cac so le: ",l)
#tong cac so chan
c=0
for i in range(1,n):
    if i%2 ==0:
        c+=i
print("tong cac so le: ",c)