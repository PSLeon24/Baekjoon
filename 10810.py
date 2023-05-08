# INPUT
n, m = map(int, input().split())
baguni = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    # baguni[i-1] ~ baguni[j-1] 에 k를 넣어!
    for n in range(i, j+1):
        baguni[n-1] = k

for i in baguni:
    print(i, end=' ')
