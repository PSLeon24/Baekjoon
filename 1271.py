import sys
money, m = map(int, sys.stdin.readline().split())

print(money // m)
print(money % m)
