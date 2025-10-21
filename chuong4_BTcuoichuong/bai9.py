#chương trình sắp xếp các giá trị của từ điển (dictionary) theo thứ tự tăng dần và giảm dần
data = {'a': 4, 'b': 2, 'c': 3, 'd': 1}
sorted_asc = dict(sorted(data.items(), key=lambda item: item[1]))
sorted_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
print("Từ điển sắp xếp theo thứ tự tăng dần:", sorted_asc)
print("Từ điển sắp xếp theo thứ tự giảm dần:", sorted_desc)
