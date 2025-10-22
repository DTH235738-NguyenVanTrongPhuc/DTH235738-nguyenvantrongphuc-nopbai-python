
file_path = 'E:/baitap6.py/bai3.txt'  # Thay đổi đường dẫn nếu cần
text_to_append = '\nĐây là dòng được thêm vào cuối tập tin.'  # Nội dung cần thêm
try:
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(text_to_append)
    print("Đã thêm nội dung vào cuối tập tin thành công.")
except FileNotFoundError:
    print(f"Tập tin không tìm thấy tại đường dẫn: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
