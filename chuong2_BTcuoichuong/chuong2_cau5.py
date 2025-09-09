so_chu = {
    0: "không",
    1: "một",
    2: "hai",
    3: "ba",
    4: "bốn",
    5: "năm",
    6: "sáu",
    7: "bảy",
    8: "tám",
    9: "chín"
}

while True:
    n = input("Nhập số nguyên dương n (tối đa 2 chữ số): ")
    if n.isdigit() and 1 <= len(n) <= 2:
        n_int = int(n)
        if n_int < 10:
            print(so_chu[n_int])
        else:
            hang_chuc = n_int // 10
            hang_don_vi = n_int % 10
            chu_chuc = so_chu[hang_chuc] + " mươi"
            if hang_don_vi == 0:
                ket_qua = chu_chuc
            elif hang_don_vi == 1:
                ket_qua = chu_chuc + " mốt"
            elif hang_don_vi == 5:
                ket_qua = chu_chuc + " lăm"
            else:
                ket_qua = chu_chuc + " " + so_chu[hang_don_vi]
            print(ket_qua)
        break
    else:
        print("Vui lòng nhập số nguyên dương có tối đa 2 chữ số!")