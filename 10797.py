tens = int(input())
nums = list(map(str, input().split()))
cnt = 0

for i in range(5):
    if nums[i] in str(tens):
        cnt += 1

print(cnt)
