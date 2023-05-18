# 다리놓기 - 조합 사용
# Combination: C(n, r) = nCr = n! / (n-r)!r! 

# Step 1. define factorial function
def factorial(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum

# Step 2. Input the test case
T = int(input())

# Step 3. Input and Output
for _ in range(T):
    r, n = map(int, input().split())
    result = int(factorial(n) / (factorial((n-r)) * factorial(r)))
    print(result)