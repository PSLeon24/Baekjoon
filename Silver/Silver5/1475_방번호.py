# Step 1. input room number N
n = list(input())
set_number = [0] * 9
idx = 0

# Step 2. (main logic) count the number of each number
for i in n:
    if i == "9":
        idx = 6
        set_number[idx] += 1
    else:
        idx = int(i)
        set_number[idx] += 1

set_number[6] = (set_number[6] + 1) // 2

# Step 3. print needed the number of room
print(max(set_number))
