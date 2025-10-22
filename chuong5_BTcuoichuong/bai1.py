
def tinh_chu_vi(a, b, c):
    return a + b + c
def tinh_dien_tich(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
def kiem_tra_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a

def kiem_tra_tam_giac_can(a, b, c):
    return a == b or b == c or a == c
def kiem_tra_tam_giac_deu(a, b, c):
    return a == b == c
def main():
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))
    if kiem_tra_tam_giac(a, b, c):
        print("Đây là tam giác.")
        chu_vi = tinh_chu_vi(a, b, c)
        dien_tich = tinh_dien_tich(a, b, c)
        print(f"Chu vi tam giác: {chu_vi}")
        print(f"Diện tích tam giác: {dien_tich}")
        if kiem_tra_tam_giac_deu(a, b, c):
            print("Đây là tam giác đều.")
        elif kiem_tra_tam_giac_can(a, b, c):
            print("Đây là tam giác cân.")
        else:
            print("Đây là tam giác thường.")
    else:
        print("Đây không phải là tam giác.")
if __name__ == "__main__":
    main()