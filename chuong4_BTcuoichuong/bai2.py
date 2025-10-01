def sinh_n_so_chinh_phuong(n):
    chinhphuong = []
    i = 0
    while len(chinhphuong) < n:
        chinhphuong.append(i * i)
        i += 1
    return chinhphuong
n= int(input("Nhập số lượng số chính phương đầu tiên cần lấy: "))
print("Các số chính phương đầu tiên là:", sinh_n_so_chinh_phuong(n))