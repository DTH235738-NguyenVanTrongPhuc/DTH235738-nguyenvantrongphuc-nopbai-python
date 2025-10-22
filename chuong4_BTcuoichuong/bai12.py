#viết hàm comnbine 2 từ điểm.
def combine_tu(tu1, tu2):
    """
    Kết hợp 2 từ thành 1 từ mới bằng cách xen kẽ các ký tự từ hai từ.
    Nếu độ dài hai từ khác nhau, phần còn lại của từ dài hơn sẽ được thêm vào cuối.
    """
    tu_moi = []
    len1, len2 = len(tu1), len(tu2)
    min_len = min(len1, len2)

    # Xen kẽ các ký tự từ hai từ
    for i in range(min_len):
        tu_moi.append(tu1[i])
        tu_moi.append(tu2[i])

    # Thêm phần còn lại của từ dài hơn
    if len1 > len2:
        tu_moi.append(tu1[min_len:])
    else:
        tu_moi.append(tu2[min_len:])

    return ''.join(tu_moi)
def main():
    tu1 = input("Nhập từ thứ nhất: ")
    tu2 = input("Nhập từ thứ hai: ")
    tu_moi = combine_tu(tu1, tu2)
    print("Từ mới sau khi kết hợp:", tu_moi)
if __name__ == "__main__":
    main()