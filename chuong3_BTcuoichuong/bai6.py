import random
import string

def tao_chuoi_ngau_nhien(do_dai):
    return ''.join(random.choices(string.ascii_lowercase, k=do_dai))
s1 = tao_chuoi_ngau_nhien(50)
s2 = tao_chuoi_ngau_nhien(50)
print("Chuỗi 1:", s1)
print("Chuỗi 2:", s2)
def longest_common_substring(s1, s2):
    m, n = len(s1), len(s2)
    max_len = 0
    ending_index = 0
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    ending_index = i
            else:
                dp[i][j] = 0
    return s1[ending_index-max_len:ending_index]
chuoi_con_chung_dai_nhat = longest_common_substring(s1, s2)
print("Chuỗi con chung dài nhất là:", chuoi_con_chung_dai_nhat)
print("Độ dài:", len(chuoi_con_chung_dai_nhat))