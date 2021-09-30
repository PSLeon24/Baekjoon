c = int(input())

for _ in range(c):
    adds = list(map(int, input().split()))
    avg = sum(adds[1:])/adds[0]
    cnt = 0
    for score in adds[1:]:
        if score > avg:
            cnt += 1
    rate = (cnt/adds[0])*100
    print(f'{rate:.3f}%')

# Do review :X
