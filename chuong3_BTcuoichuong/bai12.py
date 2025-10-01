s = input("Nhập chuỗi: ")

nguyen_am = "aeiouAEIOU"
so_in_hoa = sum(c.isupper() for c in s)
so_in_thuong = sum(c.islower() for c in s)
so_chu_so = sum(c.isdigit() for c in s)
so_khoang_trang = sum(c.isspace() for c in s)
so_ky_tu_dac_biet = sum(not c.isalnum() and not c.isspace() for c in s)
so_nguyen_am = sum(c in nguyen_am for c in s if c.isalpha())
so_phu_am = sum(c.isalpha() and c not in nguyen_am for c in s)

print("Số chữ cái in hoa:", so_in_hoa)
print("Số chữ cái in thường:", so_in_thuong)
print("Số chữ số:", so_chu_so)
print("Số ký tự đặc biệt:", so_ky_tu_dac_biet)
print("Số khoảng trắng:", so_khoang_trang)
print("Số nguyên âm:", so_nguyen_am)
print("Số phụ âm:", so_phu_am)