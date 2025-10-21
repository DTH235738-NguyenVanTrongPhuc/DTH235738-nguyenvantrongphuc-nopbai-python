from tkinter import *
def ketqua():
    a=float(labelsoa.get())
    b=float(labelsob.get())
    if a==0:
        if b==0:
            ket_qua.set("Phương trình vô số nghiệm")
        else:
            ket_qua.set("Phương trình vô nghiệm")
    else:
        ket_qua.set(f"phuong trinh co nghiem la{-b/a}")
main = Tk()
he_so_a = StringVar()
he_so_b = StringVar()
ket_qua = StringVar()
    

main.title("phuong tring bac 1")
main.geometry("400x300"+"+500+200")
Label(main,text="Phuong Trinh bac 1",font=("Arial",20),padx=80).grid(row=0,column=0,columnspan=40) 
Label(main,text="he so a:").grid(row=1,column=0)
labelsoa=Entry(main,textvariable=he_so_a)
labelsoa.grid(row=1,column=1,padx=10,pady=10)

Label(main,text="he so b:").grid(row=2,column=0)
labelsob=Entry(main,textvariable=he_so_b)
labelsob.grid(row=2,column=1,padx=10,pady=10)

btn=Button(main,text="Giải",command=ketqua).grid(row=3,column=0,columnspan=8)
btn1=Button(main,text="Tiếp",).grid(row=3,column=1,columnspan=15)
btn2=Button(main,text="Thoát",).grid(row=3,column=2,columnspan=1)

Label(main,text="Kết quả:").grid(row=4,column=0)
label=Entry(main,textvariable=ket_qua).grid(row=4,column=1,padx=10,pady=10)
main.mainloop()