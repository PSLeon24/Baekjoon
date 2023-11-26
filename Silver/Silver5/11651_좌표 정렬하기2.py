N = int(input())

coordinate = []

for _ in range(N):
    x, y = map(int, input().split())
    coordinate.append((x, y))

coordinate.sort(key=lambda x: (x[1], x[0]))

for i in coordinate:
    print(i[0], i[1])
