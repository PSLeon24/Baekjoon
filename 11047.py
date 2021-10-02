# Step 1. Input N, K
n, k = map(int, input().split())

# Step 2. Create Coins list, inputs coins.
coins = []
for _ in range(n):
    coins.append(int(input()))

# Step 3. sort coins by descending
coins.sort(reverse=True)
# print(coins)

'''
10 4200
[50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
50000 X, 10000 X, 5000 X
1000 - 4
500 - X
100 - 2
50 X, 10 X, 5 X, 1 X
'''

# Step 4. Calc
cnt = 0
for i in range(0, n):
    if coins[i] > k:
        pass
    else:
        cnt += (k//coins[i])
        k %= coins[i]

# Step 5. Print cnt
print(cnt)
