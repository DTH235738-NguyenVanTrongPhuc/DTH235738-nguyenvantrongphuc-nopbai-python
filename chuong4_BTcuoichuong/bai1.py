def sinh_n_so_chan(n):
    so_chan = []
    i = 0
    while len(so_chan) < n:
        so_chan.append(i)
        i += 2
    return so_chan

n = int(input("Nhập số lượng số chẵn đầu tiên cần lấy: "))
print("Các số chẵn đầu tiên là:", sinh_n_so_chan(n))