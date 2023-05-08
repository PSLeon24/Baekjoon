n, m = map(int, input().split())
baguni = list(range(1, n+1))

for _ in range(m):
    i, j = map(int, input().split())
    baguni[i-1:j] = baguni[i-1:j][::-1]

for i in baguni:
    print(i, end=' ')
