import math
n=int(input("nhap n: "))
s=0
for i in range (1,n+1):
    s+=i
print("tong cac so la: ",s)


m = int(input("\nNhập số tự nhiên m: "))
b = int(input("Nhập số tự nhiên b: "))
if math.gcd(m, n) == 1: #kiem tra so nguyen to cung nhau
    print("Hai số này là nguyên tố cùng nhau.")
else:
    print("Hai số này không là nguyên tố cùng nhau.")

#chuyển giây thành giờ ,phút ,giây
t=int(input("\nnhap so giây "))
gio=t//3600
phut=(t//300)%60
giay=t%60
print(f"{gio} giờ,{phut} phút ,{giay} giây")

# tham số trả lại giá trị tuyệt đối
a=float(input("nhap a: "))
b=float((input("nhap b: ")))
c=abs(a)
d=abs(b)
print("gia tri tuyet doi la: ",c)
print("gia tri tuyet doi la: ",d)
