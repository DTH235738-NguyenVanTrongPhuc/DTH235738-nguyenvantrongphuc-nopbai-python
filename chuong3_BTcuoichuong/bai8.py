s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")

if s2 in s1:
    vi_tri = s1.find(s2)
    print("Chuỗi s2 có trong s1.")
    print("Chữ cái đầu tiên của s2 nằm ở vị trí:", vi_tri)
else:
    print("Chuỗi s2 không có trong s1.")