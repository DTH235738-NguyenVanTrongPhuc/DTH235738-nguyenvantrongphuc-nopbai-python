#ham nối (concatenate) 2 từ điểm.
def noi_tu(tu1, tu2):
    """
    Nối 2 từ thành 1 từ mới
    """
    return tu1 + tu2
def main():
    tu1 = input("Nhập từ thứ nhất: ")
    tu2 = input("Nhập từ thứ hai: ")
    tu_moi = noi_tu(tu1, tu2)
    print("Từ mới sau khi nối:", tu_moi)
if __name__ == "__main__":
    main()