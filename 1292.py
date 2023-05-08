n, m = map(int, input().split())
arr = []
for i in range(1, m+1):
    for _ in range(i):
        arr.append(i)

print(sum(arr[n-1:m]))