# Hansu
# 1 ~ 9 : 한수 O
# 10 ~ 99 : 한수 O
# 103 : 3-0 != 0-1 : 한수 X
# 110 : 0-1 != 1-1 : 한수 X
# 210 : 0-1 == 1-2 : 한수 O
def hansu(num):
    # 한자리 수는 모두 한수
    # 두자리 수도 모두 한수
    if num < 100:
        return num
    elif num >= 100 and num <= 1000:
        cnt = 99
        for i in range(100, num+1):
            num_list = list(map(int, str(i)))
            if num_list[2] - num_list[1] == num_list[1] - num_list[0]:
                cnt += 1
        return cnt


n = int(input())
print(hansu(n))
