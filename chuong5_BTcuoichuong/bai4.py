
class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh
    def thong_tin(self):
        return f"Đa giác có {self.so_canh} cạnh."
class HinhBinhHanh(DaGiac):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(so_canh=4)
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)
    def tinh_dien_tich(self, chieu_cao):
        return self.chieu_dai * chieu_cao
    def thong_tin(self):
        return f"Hình bình hành với chiều dài {self.chieu_dai} và chiều rộng {self.chieu_rong}."
class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong)
    def thong_tin(self):
        return f"Hình chữ nhật với chiều dài {self.chieu_dai} và chiều rộng {self.chieu_rong}."
class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
    def thong_tin(self):
        return f"Hình vuông với cạnh {self.chieu_dai}."
def main():
    chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
    chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    hinh_chu_nhat = HinhChuNhat(chieu_dai, chieu_rong)
    print(hinh_chu_nhat.thong_tin())
    print(f"Chu vi: {hinh_chu_nhat.tinh_chu_vi()}")
    chieu_cao = float(input("Nhập chiều cao hình bình hành: "))
    print(f"Diện tích hình bình hành: {hinh_chu_nhat.tinh_dien_tich(chieu_cao)}")
    canh = float(input("Nhập cạnh hình vuông: "))
    hinh_vuong = HinhVuong(canh)
    print(hinh_vuong.thong_tin())
    print(f"Chu vi hình vuông: {hinh_vuong.tinh_chu_vi()}")
    print(f"Diện tích hình vuông: {hinh_vuong.tinh_dien_tich(canh)}")
if __name__ == "__main__":
    main()
    