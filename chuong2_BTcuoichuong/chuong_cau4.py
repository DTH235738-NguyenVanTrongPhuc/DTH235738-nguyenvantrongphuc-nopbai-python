a=int(input("nhap so a= "))
match a:
    case 1|3|5|7|8|10|12:
        print("thang",a,"co 31 ngay")
    case 4|6|9|11:
        print("thang",a,"co 30 ngay")
    case 2:
        print("thang",a,"co 28 hoac 29 ngay")
    case _:
        print("khong hop le")

