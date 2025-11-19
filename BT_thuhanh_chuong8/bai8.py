import tkinter as tk
from tkinter import messagebox

# Hàm chuyển đổi F -> C
def convert():
    try:
        f = float(entry_f.get())
        c = (f - 32) * 5 / 9
        label_result.config(text=f"{c:.2f} °C")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Chuyển đổi độ F sang độ C")
window.configure(bg="white")

# Khung chính màu vàng
frame = tk.Frame(window, bg="yellow", bd=2, relief="solid", padx=20, pady=20)
frame.pack(pady=30)

# Nhập độ F
label_f = tk.Label(frame, text="Nhập độ F", bg="yellow", font=("Arial", 12))
label_f.grid(row=0, column=0, padx=10, pady=5)

entry_f = tk.Entry(frame, width=10, fg="red", justify="center", font=("Arial", 12, "bold"))
entry_f.insert(0, "350")
entry_f.grid(row=0, column=1, padx=10, pady=5)

# Nút chuyển
btn_convert = tk.Button(frame, text="Chuyển", bg="#4682B4", fg="white", font=("Arial", 10, "bold"),
                        command=convert)
btn_convert.grid(row=1, column=0, columnspan=2, pady=10)

# Kết quả
label_text_c = tk.Label(frame, text="Độ C", bg="yellow", font=("Arial", 12))
label_text_c.grid(row=2, column=0, padx=10, pady=5)

label_result = tk.Label(frame, text="Độ C ở đây", bg="yellow", font=("Arial", 12, "bold"))
label_result.grid(row=2, column=1, padx=10, pady=5)

window.mainloop()