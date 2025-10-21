def giaithua(n):
    if n==0 or n==1:
        return 1
    else:
        return n*giaithua(n-1)
nn=int(input("Nhập n: "))
print("Giai thừa của",nn,"là:",giaithua(nn))
