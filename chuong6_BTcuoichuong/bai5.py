
file_path = 'E:/baitap6.py/bai5.txt'  # Thay đổi đường dẫn nếu cần
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
    print(f"Số dòng trong tập tin: {num_lines}")
    print(f"Số từ trong tập tin: {num_words}")
except FileNotFoundError:
    print(f"Tập tin không tìm thấy tại đường dẫn: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
