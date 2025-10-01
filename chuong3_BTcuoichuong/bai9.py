def nhap_chuoi_12():
    while True:
        s = input("Nhập chuỗi số (0-9) gồm đúng 12 ký tự: ")
        if s.isdigit() and len(s) == 12:
            return s
        else:
            print(" Chuỗi phải có đúng 12 ký tự số (0-9). Hãy nhập lại!")

chuoi = nhap_chuoi_12()
print("Chuỗi hợp lệ bạn vừa nhập là:", chuoi)