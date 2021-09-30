b = int(input())
a = int(input())
c = int(input())

result = list(str(a*b*c))
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
cnt = []
for i in range(10):
    cnt.append(0)

for i in result:
    for j in range(10):
        if i == nums[j]:
            cnt[j] += 1

for j in cnt:
    print(j)
