n =int(input("nhap nam: "))
if( n%4==0 & n%100!=0) or n%400==0:
    print(f"{n} la nam nhuan ")
else:
    print(f"{n} khong pahi nam nhuan ") 