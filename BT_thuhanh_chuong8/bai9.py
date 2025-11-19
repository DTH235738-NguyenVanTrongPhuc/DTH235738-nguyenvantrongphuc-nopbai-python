from tkinter import *

# Hàm xử lý khi nhấn nút
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen_var.get())
            screen_var.set(result)
        except ZeroDivisionError:
            screen_var.set("Lỗi chia 0")
        except:
            screen_var.set("Lỗi")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

# Cửa sổ chính
root = Tk()
root.title("Máy tính đơn giản")
root.geometry("300x400")
root.resizable(False, False)

# Biến hiển thị
screen_var = StringVar()
screen = Entry(root, textvariable=screen_var, font=("tahoma", 20), justify="right", bd=8, relief=SUNKEN)
screen.pack(fill=X, ipadx=8, ipady=8, padx=10, pady=10)

# Các nút
button_frame = Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in buttons:
    frame_row = Frame(button_frame)
    frame_row.pack()
    for btn_text in row:
        btn = Button(frame_row, text=btn_text, font=("tahoma", 16), width=5, height=2)
        btn.pack(side=LEFT, padx=3, pady=3)
        btn.bind("<Button-1>", click)

root.mainloop()