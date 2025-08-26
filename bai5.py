width = 6   # Chiều rộng hình chữ nhật
height = 4  # Chiều cao hình chữ nhật

for i in range(height):
    if i == 0 or i == height - 1:
        print("*" * width)
    else:
        print("*" + " " * (width - 2) + "*")
        