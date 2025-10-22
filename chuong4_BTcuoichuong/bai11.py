#viết hàm merge 2 từ điểm.
def merge_tu(tu1, tu2):
    """
    Merge 2 từ thành 1 từ mới bằng cách lấy nửa đầu của từ thứ nhất
    và nửa sau của từ thứ hai.
    Nếu độ dài từ lẻ, nửa đầu lấy phần lớn hơn.
    """
    mid1 = (len(tu1) + 1) // 2  # Nửa đầu của từ thứ nhất
    mid2 = len(tu2) // 2        # Nửa sau của từ thứ hai
    return tu1[:mid1] + tu2[mid2:]
def main():
    tu1 = input("Nhập từ thứ nhất: ")
    tu2 = input("Nhập từ thứ hai: ")
    tu_moi = merge_tu(tu1, tu2)
    print("Từ mới sau khi merge:", tu_moi)
if __name__ == "__main__":
    main()