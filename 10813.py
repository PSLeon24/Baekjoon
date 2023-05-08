n, m = map(int, input().split())
baguni = list(range(1, n+1))  # create baguni

for _ in range(m):
    i, j = map(int, input().split())
    temp = baguni[j-1]
    baguni[j-1] = baguni[i-1]
    baguni[i-1] = temp

for i in baguni:
    print(i, end=' ')
