def khoi_tao_list():
    """Khởi tạo list rỗng"""
    return []

def them_phan_tu(lst, phan_tu):
    """Thêm phần tử vào list"""
    lst.append(phan_tu)

def dem_so_lan_xuat_hien(lst, k):
    """Đếm số lần xuất hiện của k trong list"""
    return lst.count(k)

def la_so_nguyen_to(n):
    """Kiểm tra n có phải số nguyên tố không"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def tong_so_nguyen_to(lst):
    """Tính tổng các số nguyên tố trong list"""
    return sum(x for x in lst if la_so_nguyen_to(x))

def sap_xep_list(lst):
    """Sắp xếp list tăng dần"""
    lst.sort()

def xoa_list(lst):
    """Xóa hết phần tử trong list"""
    lst.clear()

def main():
    # Khởi tạo list
    my_list = khoi_tao_list()
    
    # Thêm phần tử
    for num in [2, 3, 5, 7, 5, 10, 5]:
        them_phan_tu(my_list, num)
    print("List sau khi thêm phần tử:", my_list)
    
    # Nhập k và đếm số lần xuất hiện
    k = 5
    print(f"Số lần xuất hiện của {k} trong list:", dem_so_lan_xuat_hien(my_list, k))
    
    # Tính tổng các số nguyên tố
    print("Tổng các số nguyên tố trong list:", tong_so_nguyen_to(my_list))
    
    # Sắp xếp list
    sap_xep_list(my_list)
    print("List sau khi sắp xếp:", my_list)
    
    # Xóa list
    xoa_list(my_list)
    print("List sau khi xóa:", my_list)

if __name__ == "__main__":
    main()
