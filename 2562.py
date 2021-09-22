# Step 1. Input Numbers
numbers = []
for i in range(9):
    n = int(input())
    numbers.append(n)

# Step 2. Find maximum and count
max = numbers[0]
cnt = 1
for i in range(len(numbers)):
    if max < numbers[i]:
        max = numbers[i]
        cnt = i+1

print(max)
print(cnt)
