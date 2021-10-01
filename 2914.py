# 평균값 = 멜로디개수 / 수록곡 갯수
# 수록곡 갯수 : a
# 평균값 i
# 멜로디개수 = 평균 * 수록곡

a, i = map(int, input().split())
print(a*(i-1)+1)
