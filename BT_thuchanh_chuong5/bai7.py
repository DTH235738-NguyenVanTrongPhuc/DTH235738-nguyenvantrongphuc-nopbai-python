def ToiUuChuoiDanhTu(s):
    # Bước 1: loại bỏ khoảng trắng đầu và cuối
    s = s.strip()
    
    # Bước 2: tách các từ (split tự động bỏ khoảng trắng dư thừa)
    words = s.split()
    
    # Bước 3: viết hoa ký tự đầu của mỗi từ
    words = [word.capitalize() for word in words]
    
    # Bước 4: ghép lại các từ bằng 1 khoảng trắng
    result = ' '.join(words)
    
    # Xuất kết quả
    print("Chuỗi sau khi tối ưu:", result)

# --- Chương trình chính ---
chuoi = input("Nhập vào một chuỗi danh từ: ")
ToiUuChuoiDanhTu(chuoi)
