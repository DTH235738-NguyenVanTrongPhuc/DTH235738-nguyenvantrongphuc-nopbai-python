s = input("nhap chuoi: ")

def ky_tu_them_it_nhat(s):
    for i in range(len(s)):
        if s[i:] == s[i:][::-1]:
            return i
    return len(s) - 1

so_ky_tu = ky_tu_them_it_nhat(s)
print("Số ký tự ít nhất cần thêm để chuỗi đối xứng là:", so_ky_tu)
print("Chuỗi đối xứng thu được:", s + s[:so_ky_tu][::-1])