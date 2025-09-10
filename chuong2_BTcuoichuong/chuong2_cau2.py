a=int(input("nhap a:"))
b=int(input("nhap b:"))
ch=input("nhap phep toan (+,-,*,/):")
if ch=="+":
    kq=a+b
    print("ket qua la:",kq)
elif ch=="-":
    kq=a-b
    print("ket qua la:",kq)
elif ch=="*":
    kq=a*b
    print("ket qua la:",kq)
elif ch=="/":
    kq=a/b
    print("ket qua la:",kq)
else:
    print("phep toan khong hop le")