import sys

money = int(sys.stdin.readline())
kinds = int(sys.stdin.readline())

prices = list(map(int, sys.stdin.readline().split()))
prices.sort(reverse=True)

if 1 not in prices:
    prices.append(1)
# print(prices)

cnt = 0
for i in range(kinds):
    if money < prices[i]:
        pass
    else:
        cnt += (money // prices[i])
        money %= prices[i]

print(cnt)

'''
위 코드는 다시 생각해봐야함.
100원을 70원, 60원, 40원, 10원으로 구하고싶으면
70, 10, 10, 10 이 되서 4가 뜸
근데 원하는 답은 60, 40 > 2
그리디알고리즘 적용안됌.
따라서 동전 교환 알고리즘, DP 공부 후 다시 도전.
'''
