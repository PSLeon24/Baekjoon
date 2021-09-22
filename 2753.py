# Step 1. Input Year
year = int(input())

# Step 2. Judge multiples
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(1)
else:
    print(0)
