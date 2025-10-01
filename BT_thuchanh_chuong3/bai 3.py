import math
a=int(input("nhap so a: "))
b=int(input("nhap so b: "))
c=int((input("nhap so c:")))
if a==0:
    if b==0:
        if c==0:
            print("phuong trinh vo so nghiem ")
        else:
            print("phuong vo nghiem ")
    else:
        print("phuong trinh co nghiem: "-c/b)
delta=b*b-4 *a*c
if delta==0:
    print("phuong trinh co nghiem kep",-b/2*a)
elif delta <0:
    print("phuong trinh vo ngiem ")
else:
    x1=(-b-math.sqrt(delta))/2*a
    x2=(-b+math.sqrt(delta))/2*a
    print(f"phuong trinh co hai nghiem \nx1={x1} \nx2={x2}")
