while True:
    s = input("Nhập dãy số tăng dần, cách nhau bởi dấu cách: ")
    try:
        lst = [float(x) for x in s.split()]
        if all(lst[i] < lst[i+1] for i in range(len(lst)-1)):
            break
        else:
            print("Dãy chưa tăng dần, vui lòng nhập lại!")
    except:
        print("Lỗi nhập liệu, nhập lại!")

print("Dãy tăng dần hợp lệ:", lst)
