# Step 1. Input A, B
a, b = map(int, input().split())

# Step 2. Compare each other.
if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('==')
