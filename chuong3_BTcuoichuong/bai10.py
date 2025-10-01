a=input("nhap vao mot chuoi thu vien se:")
def kiemtra(s):
    if "@" in s and "." in s:
        try:
            x,yz=s.split("@")
            y,z=yz.split(".")
            if x and y and z:
                return True
        except ValueError :
             return False
    return False
if kiemtra(a):
    print("chuoi dung dinh dang x@y.z")
else:
    print("chuoi khong dung dinh dang x@y.z")