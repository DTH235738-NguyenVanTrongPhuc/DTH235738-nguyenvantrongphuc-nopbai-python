#ham tính tổng và tính tích các giá trị trong từ điển(dictionary)
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
tong = sum(data.values())
tich = 1
for value in data.values():
    tich *= value
print("Tổng các giá trị trong từ điển:", tong)
print("Tích các giá trị trong từ điển:", tich)


