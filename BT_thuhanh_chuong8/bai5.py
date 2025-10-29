import tkinter as tk
from tkinter import messagebox

def change_password():
    old = entry_old.get()
    new = entry_new.get()
    confirm = entry_confirm.get()

    if old == "":
        messagebox.showwarning("Warning", "Please enter old password!")
    elif new == "":
        messagebox.showwarning("Warning", "Please enter new password!")
    elif confirm == "":
        messagebox.showwarning("Warning", "Please confirm new password!")
    elif new != confirm:
        messagebox.showerror("Error", "New passwords do not match!")
    elif old == new:
        messagebox.showwarning("Warning", "New password must be different from old password!")
    else:
        messagebox.showinfo("Success", "Password changed successfully!")
        root.destroy()

def cancel():
    root.destroy()

# Cửa sổ chính
root = tk.Tk()
root.title("Enter New Password")
root.geometry("300x150")
root.resizable(False, False)
root.configure(bg="#c0c0c0")  # màu nền kiểu Windows cổ

# Nhãn và ô nhập
tk.Label(root, text="Old Password:", bg="#c0c0c0").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="New Password:", bg="#c0c0c0").grid(row=1, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="Enter New Password Again:", bg="#c0c0c0").grid(row=2, column=0, padx=5, pady=5, sticky="e")

entry_old = tk.Entry(root, show="*", width=25)
entry_new = tk.Entry(root, show="*", width=25)
entry_confirm = tk.Entry(root, show="*", width=25)
entry_old.grid(row=0, column=1, )
entry_new.grid(row=1, column=1, )
entry_confirm.grid(row=2, column=1, )

# Nút OK và Cancel
frame_buttons = tk.Frame(root, bg="#c0c0c0")
frame_buttons.grid(row=3, column=0, columnspan=2, pady=10)

btn_ok = tk.Button(frame_buttons, text="OK", width=10, command=change_password)
btn_cancel = tk.Button(frame_buttons, text="Cancel", width=10, command=cancel)
btn_ok.grid(row=0, column=0, padx=5)
btn_cancel.grid(row=0, column=1, padx=5)

root.mainloop()
