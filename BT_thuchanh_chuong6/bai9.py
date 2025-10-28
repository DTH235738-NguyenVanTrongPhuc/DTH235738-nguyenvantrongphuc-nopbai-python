M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Phân loại
le = [x for x in M if x % 2 != 0]
chan = [x for x in M if x % 2 == 0]
nguyento = [x for x in M if is_prime(x)]
khongnt = [x for x in M if not is_prime(x)]

print("Các số lẻ:", le, f"→ Có {len(le)} số lẻ")
print("Các số chẵn:", chan, f"→ Có {len(chan)} số chẵn")
print("Các số nguyên tố:", nguyento)
print("Các số không phải nguyên tố:", khongnt)
