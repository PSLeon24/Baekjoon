X = int(input())    # 영수증에 적힌 금액
N = int(input())    # 영수증에 적힌 구매 물건 종류

money = []
cnt = []
for i in range(N):
    a, b = map(int, input().split())
    money.append(a)
    cnt.append(b)

#print(money, cnt)
sum = 0
for i in range(len(money)):
    sum += money[i] * cnt[i]

if X == sum:
    print('Yes')
else:
    print('No')
# print(sum)
# 4000 4000
