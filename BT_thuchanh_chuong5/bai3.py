def DemSoChan():
    s = input("Nhập chuỗi các số (cách nhau bởi dấu ;): ")
    arr = s.split(';')           # Tách các phần tử
    so_chan = 0

    print("\nCác số trong chuỗi:")
    for x in arr:
        n = int(x)               # Chuyển chuỗi thành số nguyên
        print(n)
        if n % 2 == 0:
            so_chan += 1

    print(f"\nCó {so_chan} số chẵn trong chuỗi.")

# --- Chạy chương trình ---
DemSoChan()
