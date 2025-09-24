n=input("nhap chuoi gom chu cai va chu so: ")
print("chuoi dao nguoc la: ",n[::-1])
print("so luong cac chu cai trong chuoi la :",sum(c.isalpha() for c in n))
print("so luong cac chu so trong chuoi la: ",sum(c.isdigit() for c in n))
