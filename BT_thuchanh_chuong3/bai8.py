a=int(input("nhap so a: "))
b=int(input("nhap so b: "))
tinh=input("chon phep toan(-,+,*,/): ")
if tinh=='-':
    print(f"{a} - {b} =",a-b)
elif tinh=='+':
    print(f"{a} + {b} =",a+b)
elif tinh=='*':
    print(f"{a} * {b} =",a*b)
elif tinh=='/':
    print(f"{a} / {b} =",a/b)
else:
    print("chon phep tinh khong hop le")