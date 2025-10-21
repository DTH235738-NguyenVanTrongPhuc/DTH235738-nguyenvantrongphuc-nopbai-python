boi_cua_3 = [x for x in range(100) if x % 3 == 0]
print(boi_cua_3)

# a) Dãy 20 số chính phương đầu tiên
square_numbers = [i**2 for i in range(1, 21)]
print("\nDãy 20 số chính phương đầu tiên:")
print(square_numbers)

# b) Dãy 10 chuỗi nhị phân theo quy luật: 1, 10, 100, ...
binary_strings = ['1' + '0'*i for i in range(10)]
print("\nDãy 10 chuỗi nhị phân theo quy luật 1, 10, 100, ...:")
print(binary_strings)
binary_shift = ['0'*i + '1' + '0'*(9 - i) for i in range(10)]
print("Dãy 10 chuỗi nhị phân theo quy luật dịch bit:")
for b in binary_shift:
    print(b)