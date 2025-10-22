
file_path = 'E:/baitap6.py/bai6.txt'  # Thay đổi đường dẫn nếu cần
from collections import defaultdict
word_count = defaultdict(int)
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_count[word] += 1
    print("Tần suất xuất hiện của mỗi từ trong tập tin:")
    for word, count in word_count.items():
        print(f"'{word}': {count}")
except FileNotFoundError:
    print(f"Tập tin không tìm thấy tại đường dẫn: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
