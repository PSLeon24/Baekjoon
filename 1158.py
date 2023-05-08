n, k = map(int, input().split())
arr = [i for i in range(1, n+1)] # original members

answer = []
del_idx = 0

for i in range(n):
    del_idx += (k-1)
    if del_idx >= len(arr):
        del_idx %= len(arr)
    answer.append(str(arr[del_idx]))
    arr.pop(del_idx)

print(f"<{', '.join(answer)}>")