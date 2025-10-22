def Tinhchuvi(a,b):
    return (a+b)*2
def Tinhdientich(a,b):
    return a*b
def main():
    a=float(input("Nhập chiều dài: "))
    b=float(input("Nhập chiều rộng: "))
    chuvi= Tinhchuvi(a,b)
    dientich= Tinhdientich(a,b)
    print(f"Chu vi hình chữ nhật là: {chuvi}")
    print(f"Diện tích hình chữ nhật là: {dientich}")
if __name__ == "__main__":
    main()