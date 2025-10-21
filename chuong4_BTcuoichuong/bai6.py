import random

def khoi_tao_list_ngau_nhien(n, start=0, end=100):
    """
    Khởi tạo list ngẫu nhiên n phần tử trong khoảng start đến end (bao gồm cả hai)
    """
    return [random.randint(start, end) for _ in range(n)]

def xoa_phan_tu(lst, k):
    """
    Xóa tất cả phần tử có giá trị k khỏi list
    """
    # Cách 1: tạo list mới chỉ chứa các phần tử != k
    # lst[:] = [x for x in lst if x != k]  # sửa list gốc
    # Cách 2: dùng vòng while xóa trực tiếp
    while k in lst:
        lst.remove(k)

def kiem_tra_doi_xung(lst):
    """
    Kiểm tra list có đối xứng (palindrome) không
    Trả về True nếu đối xứng, False nếu không
    """
    return lst == lst[::-1]

def main():
    n = int(input("Nhập số phần tử n: "))
    my_list = khoi_tao_list_ngau_nhien(n, 0, 20)
    print("List ngẫu nhiên:", my_list)

    k = int(input("Nhập giá trị k cần xóa: "))
    xoa_phan_tu(my_list, k)
    print(f"List sau khi xóa tất cả phần tử bằng {k}:", my_list)

    if kiem_tra_doi_xung(my_list):
        print("List có đối xứng.")
    else:
        print("List không đối xứng.")

if __name__ == "__main__":
    main()
