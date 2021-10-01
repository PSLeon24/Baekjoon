from math import factorial

n, k = map(int, input().split())
result = (factorial(n) // (factorial(k) * factorial(n-k))) % 10007
print(int(result))
