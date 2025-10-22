
def NegativeNumberInStrings(s):
    num = ''
    result = []

    i = 0
    while i < len(s):
        # Nếu gặp dấu '-' và ký tự sau là số
        if s[i] == '-' and i + 1 < len(s) and s[i + 1].isdigit():
            num = '-'
            i += 1
            # Lấy toàn bộ các chữ số liền sau dấu '-'
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            result.append(int(num))
        else:
            i += 1

    # Xuất kết quả
    if result:
        print("Các số nguyên âm trong chuỗi là:", *result)
    else:
        print("Không có số nguyên âm trong chuỗi.")

# --- Chương trình chính ---
chuoi = input("Nhập vào một chuỗi bất kỳ: ")
NegativeNumberInStrings(chuoi)