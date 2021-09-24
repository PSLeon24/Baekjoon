# Step 1. Input 10 numbers
numbers = []
for i in range(10):
    numbers.append(int(input()))
    # Step 1_2. save (numbers mod 42)
    numbers[i] = numbers[i] % 42

# Step 3. Create temp, cnt variable
temp = set(numbers)
cnt = len(temp)

# Print!
print(cnt)
