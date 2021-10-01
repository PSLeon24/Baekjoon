import sys

su = list(map(int, sys.stdin.readline().split()))
result = 0
for i in su:
    result += i**2

print(result % 10)
