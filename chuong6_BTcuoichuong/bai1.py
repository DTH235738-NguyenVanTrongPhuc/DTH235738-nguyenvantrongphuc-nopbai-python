
file_path = 'E:/baitap6.py/example.txt'  # Thay đổi đường dẫn nếu cần
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Tập tin không tìm thấy tại đường dẫn: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")


