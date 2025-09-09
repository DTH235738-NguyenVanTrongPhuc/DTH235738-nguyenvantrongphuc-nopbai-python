n=int(input("nhap so n= "))
if n>1 and n<9:
    print(f"bang cuu chung cua {n} la: ")
    for i in range (1,11):
        print(f"{n} x {i} =",n*i)
else:
    print("khong hop le")

