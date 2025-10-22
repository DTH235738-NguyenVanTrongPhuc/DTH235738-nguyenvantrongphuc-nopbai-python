def Tinhchuvi(h,r):
    return 2*3.14*r*h
def Tinhdientich(r):
    return 2*3.14*r*r+2*3.14*r*h
def main():
    r=float(input("Nhập bán kính đáy: "))
    h=float(input("Nhập chiều cao: "))
    chuvi= Tinhchuvi(h,r)
    dientich= Tinhdientich(r)
    print(f"Chu vi hình trụ là: {chuvi}")
    print(f"Diện tích hình trụ là: {dientich}")
if __name__ == "__main__":
    main()
