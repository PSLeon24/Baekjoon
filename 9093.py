t = int(input())

for _ in range(t):
    words = list(input().split())
    for j in words:
        print(j[:: -1], end=' ')
    print('\n')
