import tkinter as tk

root = tk.Tk()
root.title("frame 2")

# Tạo nhãn tiêu đề cho từng hàng borderwidth
for bw in range(5):
    # Hiển thị dòng mô tả độ dày border
    tk.Label(root, text=f"borderwidth = {bw}", width=15).grid(row=bw, column=0, padx=5, pady=5)

    # Tạo 6 khung với các kiểu border khác nhau
    for i, relief in enumerate(["raised", "sunken", "flat", "ridge", "groove", "solid"]):
        frame = tk.Frame(root, borderwidth=bw, relief=relief, width=60, height=30, bg="#d9d9d9")
        frame.grid(row=bw, column=i + 1, padx=5, pady=5)
        frame.grid_propagate(False)  # Giữ kích thước cố định

        # Thêm nhãn tên kiểu border vào giữa khung
        label = tk.Label(frame, text=relief, bg="#d9d9d9")
        label.pack(expand=True)

root.mainloop()
