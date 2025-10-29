import tkinter as tk

# Hàm xử lý khi nhấn nút
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except Exception:
            screen.set("Error")
    elif text == "Clr":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# Cửa sổ chính
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)  # Không cho thay đổi kích thước

# Biến hiển thị màn hình
screen = tk.StringVar()
entry = tk.Entry(
    root,
    textvariable=screen,
    font=("Arial", 18),
    bd=5,
    relief="sunken",
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=5, pady=5, sticky="nsew")

# Danh sách nút (theo hàng)
buttons = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["-", "0", "."],
    ["+", "-", "*", "/", "="],
    ["Clr"]
]

# Tạo và sắp xếp các nút cân đối
row_index = 1
for row in buttons:
    col_index = 0
    for char in row:
        btn = tk.Button(
            root,
            text=char,
            font=("Arial", 14, "bold"),
            width=5,
            height=2,
            relief="raised",
            bd=3,
            bg="#f0f0f0",
            activebackground="#d9d9d9"
        )
        btn.grid(row=row_index, column=col_index, padx=3, pady=3, sticky="nsew")
        btn.bind("<Button-1>", click)
        col_index += 1
    row_index += 1

# Cân chỉnh khung lưới (đều nhau)
for i in range(4):
    root.columnconfigure(i, weight=1, uniform="col")
for i in range(row_index):
    root.rowconfigure(i, weight=1, uniform="row")

root.mainloop()
