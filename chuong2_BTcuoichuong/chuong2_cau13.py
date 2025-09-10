import math
import sys
a=int(input("nhap a: "))
b=int(input("nhap b: "))
c=int(input("nhap c: "))
if a==0:
    if b==0:
        if c==0:
            print("phuong trinh vo so nghiem")
        else: 
            print("phuong trinh vo nghiem")
    else:
        print("phuong co mot nghiem ",-c/b)
    sys.exit()
delta=b*b-4 *a*c
if delta:
    print("phuong vo nghiem")
elif delta==0:
    print("phuong trinh co mot nghiem kep",-b/2*a)
else:
    x1=(-b+math.sqrt(delta)/2*a)
    x2=(-b-math.sqrt(delta)/2*a)
    print("nghiem cua x1 = ",x1)
    print("nghiem cua x2 = ",x2)