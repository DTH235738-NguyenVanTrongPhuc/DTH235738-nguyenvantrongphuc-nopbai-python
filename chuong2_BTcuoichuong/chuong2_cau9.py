n=int(input("nhap so nguyen n: "))
s =0
s1=0
s2=0
s3=0
s4=0
print("n la : ",n)
for i in range (1,n+1):
        s1= s1 + i        
print("kết quả của la 2n-1: ",s1)
for i in range (1,n+1):
        if i%2==0:
            s2=s2+i;
print("của 2n la: ",s2)
for i in range (1,n+1):
       s3=s3+i*i
print("của n^2 la: ",s3)
for i in range (1,n+1):
       s4=s4+1/i
print("của 1/n la: ",s4)
       



