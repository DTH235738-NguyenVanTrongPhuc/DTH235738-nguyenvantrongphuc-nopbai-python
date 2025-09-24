n = int(input("Nhập chiều dài chuỗi nhị phân: "))

def sinh_nhiphan(chuoi, do_dai):
    if len(chuoi) == do_dai:
        print(chuoi)
        return
    sinh_nhiphan(chuoi + "0", do_dai)
    sinh_nhiphan(chuoi + "1", do_dai)

sinh_nhiphan("", n)
