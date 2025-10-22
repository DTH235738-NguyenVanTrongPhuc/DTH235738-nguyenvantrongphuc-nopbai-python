
file_path = 'E:/baitap6.py/bai4.txt'  # Thay đổi đường dẫn nếu cần
n = 5  # Số dòng cần đọc từ cuối tập tin
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        last_n_lines = lines[-n:]  # Lấy n dòng cuối cùng
        for line in last_n_lines:
            print(line.strip())
except FileNotFoundError:
    print(f"Tập tin không tìm thấy tại đường dẫn: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
