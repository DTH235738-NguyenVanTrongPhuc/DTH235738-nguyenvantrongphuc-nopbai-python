thang=int(input("nhap thang: "))
if thang in(1,3,5,7,8,10,12) :
    print(f"thang {thang} co 31 ngay ")
elif thang in(4,6,9,11):
    print(f"thang {thang } co 30 ngay")
elif thang == 2:
    nam=int(input("nhap nam kiem tra nam nhuan: "))
    if(nam%4==0 & nam% 100!=0) or nam %400==0:
        print(f"thang {thang} co 28 ngay ")    
    else:
        print(f"thang {thang} co 28 ngay ")
else :
    print("nhap so thang khong hop le ")