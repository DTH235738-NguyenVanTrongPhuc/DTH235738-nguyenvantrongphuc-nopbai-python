from tkinter import *

# Danh sách Can và Chi
can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

# Hàm xử lý chuyển đổi
def chuyenNam():
    try:
        namDL = int(stringNamDL.get())
        can_index = namDL % 10
        chi_index = namDL % 12
        namAL = can[can_index] + " " + chi[chi_index]
        stringNamAL.set(namAL)
    except:
        stringNamAL.set("Dữ liệu không hợp lệ!")

# Tạo cửa sổ
root = Tk()
root.title("Chuyển năm Dương lịch sang Âm lịch")
root.configure(bg="yellow")
root.geometry("400x200")
root.resizable(False, False)

# Biến lưu dữ liệu
stringNamDL = StringVar()
stringNamAL = StringVar()

# Giao diện
Label(root, text="Nhập năm dương:", bg="yellow", font=("tahoma", 12)).grid(row=0, column=0, padx=10, pady=15, sticky=E)
Entry(root, width=15, textvariable=stringNamDL, font=("tahoma", 12)).grid(row=0, column=1)
Button(root, text="Chuyển", width=10, bg="lightblue", command=chuyenNam).grid(row=0, column=2, padx=10)

Label(root, text="Năm âm:", bg="yellow", font=("tahoma", 12)).grid(row=1, column=0, sticky=E)
Entry(root, width=20, textvariable=stringNamAL, font=("tahoma", 12)).grid(row=1, column=1, columnspan=2, pady=10)

root.mainloop()