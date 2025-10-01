import math

n=int(input("nhap so: "))
def snt(n):
    if(n<2):
        return 0
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
         
if snt(n):
   print(f"{n} so ngyen to")
else:
   print(f"{n} khong phai  a so nguyen to")
    
            