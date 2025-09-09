ls = 0
print("Nhap so tien: ")
x = float(input())
for i in range(1,19):
    ls += x*(0.6/100)
    if(i%6==0):
        x = x + ls
        ls=0
print("So tien nhan duoc sau 18 thang la: ", x)

