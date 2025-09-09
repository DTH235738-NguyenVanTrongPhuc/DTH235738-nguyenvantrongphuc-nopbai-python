import math
a=float(input("nhap so a= "))
b=float(input("nhap so b= "))
c=float(input("nhap so c= "))

if a==0:
    if b==0:
        if c==0:
            print("phuong trinh  vo so  nghiem")
        else:
            print("phuong trinh vo  nghiem")
    else: 
        print("phuong trinh co mot nghiem",-c/b)
deta=b**2-4*a*c
if deta<0:
    print("phuong trinh vo nghiem")
elif deta==0:
    print("phuong trinh co mot nghiem kep",-b/(2*a))
else:
    x1=(-b+math.sqrt(deta))/(2*a)
    x2=(-b-math.sqrt(deta))/(2*a)
    print("phuong trinh co hai nghiem phan biet",x1,x2)



    