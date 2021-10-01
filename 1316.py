# Step 1. Input N, create result
n = int(input())
result = n

# Step 2. Repeat N, Input word, compare word[i] with word[i+1]
for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:  # 지금 위치와 다음 위치 알파벳이 같으면,
            result -= 1
            break

# Step 3. Print result.
print(result)
