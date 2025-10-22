
file_path = 'E:/baitap6.py/bai2.txt'  # Thay đổi đường dẫn nếu cần
n = 5  # Số dòng cần đọc
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break  # Dừng nếu đã đọc hết tập tin
            print(line.strip())
except FileNotFoundError:
    print(f"Tập tin không tìm thấy tại đường dẫn: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")