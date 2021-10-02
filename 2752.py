num = list(map(int, input().split()))

tmp = max(num)
for i in range(len(num)-1):
    for j in range(len(num)-i-1):
        if num[j] > num[j+1]:
            tmp = num[j]
            num[j] = num[j+1]
            num[j+1] = tmp

for i in num:
    print(i, end=' ')


# 간단하게 하면
'''
num = list(map(int, input().split()))
num.sort()
for i in num:
    print(i, end=' ')
'''
